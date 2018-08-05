""" sandbox """
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# -*- coding: utf-8 -*-
import json
from os import path
from pathlib import Path
from pprint import pprint

from models import Role, User
from utils.mock import set_from_mock

def do_sandbox():

    #USER
    json_path = Path(path.dirname(path.realpath(__file__))) / '..' / 'mock' / 'jsons' / 'users.json'
    with open(json_path) as json_file:
        for (index, user_dict) in enumerate(json.load(json_file)):
            query = User.query.filter_by(email=user_dict['email'])
            if query.count() == 0:
                user = User(from_dict=user_dict)
                user.validationToken = None
                user.check_and_save_itself()
                set_from_mock("thumbs", user, index + 1)
                print("CREATED user")
                pprint(vars(user))

                if 'role' in user_dict:
                    role = Role()
                    role.type = user_dict['role']
                    role.user = user
                    role.check_and_save_itself()
                    print("CREATED role")
                    pprint(vars(role))
