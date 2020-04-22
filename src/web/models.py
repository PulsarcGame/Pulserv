import mongoengine


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
    userName = mongoengine.StringField()
    email = mongoengine.EmailField()  # Will need to perform additional validation on this.
    passwordHash = mongoengine.StringField()

    thirdPartyPlatformCredentials = mongoengine.DictField()  # Storing OAuth keys, etc.

    def setPassword(self, password):
        pass

    def checkPassword(self, passwordHash):
        pass
