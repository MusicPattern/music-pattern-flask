""" credentials """
from flask_login import login_user

from models.utils import ApiErrors
from models import User

def get_user_with_credentials(identifier, password):
    errors = ApiErrors()
    errors.status_code = 401

    print('identifier, password', identifier, password)

    if identifier is None:
        errors.addError('identifier', 'Identifier is missing')
    if password is None:
        errors.addError('password', 'Password is missing')
    errors.maybeRaise()

    user = User.query.filter_by(email=identifier).first()

    if not user:
        errors.addError('identifier', 'Wrong identifier')
        raise errors
    #if not user.isValidated:
    #    errors.addError('identifier', "This account is not validated")
    #    raise errors
    if not user.checkPassword(password):
        errors.addError('password', 'Wrong password')
        raise errors

    login_user(user, remember=True)
    return user

def change_password(user, password):
    if type(user) != User:
        user = User.query.filter_by(email=user).one()
    user.setPassword(password)
    user.save()
