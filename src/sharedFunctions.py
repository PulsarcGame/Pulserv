from usernames import is_safe_username
from email_validator import validate_email, EmailNotValidError


def usernameValid(username):
    if len(username) > 12 or len(username) < 1:
        return "Invalid Username! Must be between 1 and 12 characters."
    if is_safe_username(username):
        # Extensible by inserting more logic in here!
        return True
    else:
        return "Username not allowed!"


def emailValid(email):
    try:
        validate_email(email, allow_smtputf8=False)
        return True
    except EmailNotValidError as error:
        return str(error)


def passwordValid(password):
    return True
