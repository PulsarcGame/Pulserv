import mongoengine
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_hex


def tokenWrapper():
    return token_hex(64)


class Map(mongoengine.Document):
    name = mongoengine.StringField()
    iconURL = mongoengine.URLField()
    difficulty = mongoengine.DecimalField()
    description = mongoengine.StringField()
    source = mongoengine.StringField()  # Allowed inputs: native, mania, intralism
    tags = mongoengine.ListField()  # Unsure about this... TODO: Clarify tag system
    directDL = mongoengine.URLField()


class Tag(mongoengine.Document):
    name = mongoengine.StringField()
    filterable = mongoengine.BooleanField()


class Player(mongoengine.Document):
    username = mongoengine.StringField()
    email = mongoengine.EmailField()  # Will need to perform additional validation on this.
    passwordHash = mongoengine.StringField()

    thirdPartyPlatformCredentials = mongoengine.DictField()  # Storing OAuth keys, etc.

    def setPassword(self, password):
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.passwordHash, password)


class AuthToken(mongoengine.Document):
    key = mongoengine.StringField(max_length=128, default=tokenWrapper)
    player = mongoengine.ReferenceField(Player, required=True)
    scope = mongoengine.StringField(default="read")

    # A method for checking tokens...
    # Returns False, or tokenObject.
    @staticmethod
    def checkToken(token=None):
        tokenObject = AuthToken.objects.get(key=token)
        if tokenObject is None:
            return False
        else:
            return tokenObject
