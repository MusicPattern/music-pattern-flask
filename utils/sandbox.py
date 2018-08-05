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
from utils.scales import get_scale_note_indexes_combinations

def do_sandbox():

    #USER
    json_path = Path(path.dirname(path.realpath(__file__))) / '..' / 'mock' / 'jsons' / 'users.json'
    with open(json_path) as json_file:
        for (user_index, user_dict) in enumerate(json.load(json_file)):
            query = User.query.filter_by(email=user_dict['email'])
            if query.count() == 0:
                user = User(from_dict=user_dict)
                user.validationToken = None
                user.check_and_save_itself()
                set_from_mock("thumbs", user, user_index + 1)
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
        for (harmony_index, harmony_dict) in enumerate(json.load(json_file)):
            query = Harmony.query.filter_by(name=harmony_dict['name'])
            if query.count() == 0:
                harmony = Harmony(from_dict=harmony_dict)
                harmony.check_and_save_itself()
                print("CREATED harmony")
                pprint(vars(harmony))
            else:
                harmony = query.first()

            #NOTE
            notes = []
            for note_index in range(harmony.notesMaxLength):
                query = Note.query.filter_by(index=note_index)
                if query.count() == 0:
                    note = Note(from_dict={ "index": note_index })
                    note.check_and_save_itself()
                    print("CREATED note")
                    pprint(vars(note))
                else:
                    note = query.first()
                notes.append(note)

            #PITCH
            note_index=0
            for index in range(harmony.pitchesMaxLength):
                query = Pitch.query.filter_by(index=index)
                if query.count() == 0:
                    pitch = Pitch(from_dict={ "index": index })
                    pitch.note = notes[note_index]
                    pitch.check_and_save_itself()
                    print("CREATED pitch")
                    pprint(vars(pitch))
                note_index+=1
                if note_index == harmony.notesMaxLength:
                    note_index = 0

            #SCALE
            scale_note_indexes_combinations = get_scale_note_indexes_combinations(7, harmony.name)
            scale_note_indexes_combinations_length = str(len(scale_note_indexes_combinations))
            for (scale_index, scale_note_indexes) in enumerate(scale_note_indexes_combinations):
                query = Scale.query.filter_by(
                    combinationIndex=scale_index,
                    harmonyId=harmony.id
                )
                if query.count() == 0:
                    scale = Scale()
                    scale.combinationIndex = scale_index
                    scale.harmony = harmony
                    scale.check_and_save_itself()
                    print("CREATED scale " + str(scale_index) + " / " + scale_note_indexes_combinations_length)
                    #pprint(vars(scale))
                    for scale_note_index in scale_note_indexes:
                        note = notes[scale_note_index]
                        scale_note = ScaleNote()
                        scale_note.scale = scale
                        scale_note.note = note
                        scale_note.check_and_save_itself()
                        #print("CREATED scale_note")
                        #pprint(vars(scale_note))
