""" sandbox """
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# -*- coding: utf-8 -*-
import json
from os import path
from pathlib import Path
from pprint import pprint

from models import Harmony,\
                   Note,\
                   Pitch,\
                   Role,\
                   Scale,\
                   ScaleNote,\
                   User
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

    #HARMONY
    json_path = Path(path.dirname(path.realpath(__file__))) / '..' / 'mock' / 'jsons' / 'harmonies.json'
    with open(json_path) as json_file:
        for (index, harmony_dict) in enumerate(json.load(json_file)):
            query = Harmony.query.filter_by(name=harmony_dict['name'])
            if query.count() == 0:
                harmony = Harmony(from_dict=harmony_dict)
                harmony.check_and_save_itself()
                print("CREATED harmony")
                pprint(vars(harmony))
            else:
                harmony = query.first()

            #NOTE
            for index in range(harmony.notesMaxLength):
                query = Note.query.filter_by(index=index)
                if query.count() == 0:
                    note = Note(from_dict={ "index": index })
                    note.check_and_save_itself()
                    print("CREATED note")
                    pprint(vars(note))

            """
            #PITCH
            for index in range(PITCHES_MAX_LENGTH):
                query = Pitch.query.filter_by(index=index)
                if query.count() == 0:
                    pitch = Pitch(from_dict={ "index": index })
                    pitch.check_and_save_itself()
                    print("CREATED pitch")
                    pprint(vars(pitch))

            #SCALE
            for index in range(SCALES_MAX_LENGTH):
                query = Scale.query.filter_by(index=index)
                if query.count() == 0:
                    scale = Scale(from_dict={ "size": index })
                    scale.check_and_save_itself()
                    print("CREATED scale")
                    pprint(vars(scale))
            """
