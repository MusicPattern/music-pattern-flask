""" login_manager """
from flask_login import LoginManager
from flask import current_app as app, jsonify

from models.utils import ApiErrors
from models import User
from utils.credentials import get_user_with_credentials

login_manager = LoginManager()
login_manager.init_app(app)

app.config['REMEMBER_COOKIE_DURATION'] = 365 * 24 * 3600

@app.login_manager.user_loader
def get_user_with_id(user_id):
    return User.query.get(user_id)


@app.login_manager.request_loader
def get_user_with_request(request):
    auth = request.authorization
    if not auth:
        return None
    user = get_user_with_credentials(auth.username, auth.password)
    return user


@app.login_manager.unauthorized_handler
def send_401():
    e = ApiErrors()
    e.addError('global', 'Authentification is needed')
    return jsonify(e.errors), 401
