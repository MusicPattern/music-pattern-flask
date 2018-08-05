"""users routes"""
from flask_login import current_user, login_required, logout_user, login_user
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy.sql.expression import and_
from flask import current_app as app, jsonify, request
import gspread

from models import Role, User, Wrapper
from utils.credentials import get_user_with_credentials
from utils.includes import USER_INCLUDES
from utils.rest import expect_json_data,\
                       handle_rest_get_list, \
                       login_or_api_key_required
from utils.search import get_search_filter

def make_user_query():
    query = User.query
    return query

@app.route("/users/current", methods=["GET"])
@login_required
def get_profile():
    user = current_user.asdict(include=USER_INCLUDES)
    return jsonify(user)


@app.route("/users", methods=["GET"])
@login_required
def get_users():

    query = User.query

    roles = request.args.get('roles', '').split(',')
    query = query.filter(and_(*[User.roles.any(Role.type == role) for role in roles]))

    search = request.args.get('search')
    if search is not None:
        query = query.filter(get_search_filter([User], search))

    return handle_rest_get_list(User,
                                include=USER_INCLUDES,
                                query=query,
                                page=request.args.get('page'),
                                paginate=10,
                                order_by='id desc')

@app.route('/users/current', methods=['PATCH'])
@login_or_api_key_required
@expect_json_data
def patch_profile():
    current_user.populateFromDict(request.json)
    Wrapper.check_and_save(current_user)
    return jsonify(current_user.asdict(include=USER_INCLUDES)), 200


@app.route("/users/signin", methods=["POST"])
def signin():
    json = request.get_json()
    identifier = json.get("identifier")
    password = json.get("password")
    user = get_user_with_credentials(identifier, password)
    return jsonify(user.asdict(include=USER_INCLUDES)), 200


@app.route("/users/signout", methods=["GET"])
@login_required
def signout():
    logout_user()
    return jsonify({"global": "Deconnecté"})


@app.route("/users", methods=["POST"])
def signup():
    new_user = User(from_dict=request.json)
    new_user.id = None
    Wrapper.check_and_save(new_user)
    login_user(new_user)
    return jsonify(new_user._asdict(include=USER_INCLUDES)), 201
