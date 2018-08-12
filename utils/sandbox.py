""" sandbox """
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# -*- coding: utf-8 -*-
from pprint import pprint

from mock.scripts import bar_mocks,\
                         bar_voice_mocks,\
                         harmony_mocks,\
                         melody_mocks,\
                         score_mocks,\
                         score_staff_mocks,\
                         staff_mocks,\
                         staff_bar_mocks,\
                         rhythm_mocks,\
                         user_mocks,\
                         voice_mocks
from models.utils import Wrapper
from models import Bar,\
                   BarVoice,\
                   Harmony,\
                   Melody,\
                   Note,\
                   Pitch,\
                   Rhythm,\
                   Role,\
                   Scale,\
                   ScaleNote,\
                   Score,\
                   Staff,\
                   StaffBar,\
                   User,\
                   Voice

from utils.mock import set_from_mock


def do_sandbox():

    #USER
    users = []
    for (user_index, user_mock) in enumerate(user_mocks):
        query = User.query.filter_by(email=user_mock['email'])
        if query.count() == 0:
            user = User(from_dict=user_mock)
            user.validationToken = None
            Wrapper.check_and_save(user)
            set_from_mock("thumbs", user, user_index + 1)
            print("CREATED user")
            pprint(vars(user))

            if 'role' in user_mock:
                role = Role()
                role.type = user_mock['role']
                role.user = user
                Wrapper.check_and_save(role)
                print("CREATED role")
                pprint(vars(role))
        else:
            user = query.first()
        users.append(user)

    #HARMONY
    for (harmony_index, harmony_mock) in enumerate(harmony_mocks):
        query = Harmony.query.filter_by(name=harmony_mock['name'])
        if query.count() == 0:
            harmony = Harmony(from_dict=harmony_mock)
            Wrapper.check_and_save(harmony)
            print("CREATED harmony")
            pprint(vars(harmony))
        else:
            harmony = query.first()

        #NOTE
        notes = []
        for note_index in range(harmony.notesMax):
            query = Note.query.filter_by(index=note_index)
            if query.count() == 0:
                note = Note(from_dict={ "index": note_index })
                if "noteNames" in harmony_mock and note_index in harmony_mock['noteNames']:
                    note.name = harmony_mock['noteNames'][note_index]
                Wrapper.check_and_save(note)
                print("CREATED note")
                pprint(vars(note))
            else:
                note = query.first()
            notes.append(note)

        #PITCH
        note_index = 0
        for index in range(harmony.pitchesMax):
            query = Pitch.query.filter_by(index=index)
            if query.count() == 0:
                pitch = Pitch(from_dict={ "index": index })
                pitch.note = notes[note_index]
                Wrapper.check_and_save(pitch)
                print("CREATED pitch")
                pprint(vars(pitch))
            note_index+=1
            if note_index == harmony.notesMax:
                note_index = 0

        #SCALE
        #for scaleSize in range(1, harmony.scaleMaxSize):
        for scaleSize in []:
            scale_note_indexes_combinations = harmony.get_scale_note_indexes_combinations(scaleSize)
            scale_note_indexes_combinations_length = str(len(scale_note_indexes_combinations))
            for (scale_index, scale_note_indexes) in enumerate(scale_note_indexes_combinations):
                query = Scale.query.filter_by(
                    combinationIndex=scale_index,
                    harmonyId=harmony.id,
                    size=scaleSize
                )
                if query.count() == 0:
                    scale = Scale()
                    scale.combinationIndex = scale_index
                    scale.harmony = harmony
                    scale.name = harmony_mock['get_scale_name'](scale_note_indexes)
                    scale.tags = harmony_mock['get_scale_tags'](scale_note_indexes)
                    scale.size = scaleSize
                    Wrapper.check_and_save(scale)
                    print("CREATED scale " + str(scale_index) + " / " + scale_note_indexes_combinations_length + "(" + str(scaleSize) + ")")
                    #pprint(vars(scale))
                    for scale_note_index in scale_note_indexes:
                        note = notes[scale_note_index]
                        scale_note = ScaleNote()
                        scale_note.scale = scale
                        scale_note.note = note
                        Wrapper.check_and_save(scale_note)
                        #print("CREATED scale_note")
                        #pprint(vars(scale_note))

        #MELODY
        melodies = []
        for melody_mock in melody_mocks:
            query = Melody.query.filter_by(pattern=melody_mock['pattern'])
            if query.count() == 0:
                melody = Melody(from_dict=melody_mock)
                Wrapper.check_and_save(melody)
                print("CREATED melody")
                pprint(vars(melody))
            else:
                melody = query.first()
            melodies.append(melody)

        #RHYTHM
        rhythms = []
        for rhythm_mock in rhythm_mocks:
            query = Rhythm.query.filter_by(pattern=rhythm_mock['pattern'])
            if query.count() == 0:
                rhythm = Rhythm(from_dict=rhythm_mock)
                Wrapper.check_and_save(rhythm)
                print("CREATED rhythm")
                pprint(vars(rhythm))
            else:
                rhythm = query.first()
            rhythms.append(rhythm)

        #SCORE
        scores = []
        for score_mock in score_mocks:
            query = Score.query.filter_by(name=score_mock['name'])
            if query.count() == 0:
                score = Score(from_dict=score_mock)
                user = users[score_mock['userIndex']]
                score.user = user
                Wrapper.check_and_save(score)
                print("CREATED score")
                pprint(vars(score))
            else:
                score = query.first()
            scores.append(score)

        #STAFF
        staves = []
        for staff_mock in staff_mocks:
            query = Staff.query.filter_by(
                positionIndex=staff_mock['positionIndex'],
                scoreId=score.id
            )
            if query.count() == 0:
                staff = Staff(from_dict=staff_mock)
                Wrapper.check_and_save(staff)
                print("CREATED staff")
                pprint(vars(staff))
            else:
                staff = query.first()
            staves.append(staff)

        #SCORE STAFF
        for score_staff_mock in score_staff_mocks:
            score = scores[score_staff_mock['scoreIndex']]
            staff = staves[score_staff_mock['staffIndex']]
            query = Staff.query.filter_by(
                positionIndex=score_staff_mock['positionIndex'],
                scoreId=score.id,
                staffId=staff.id
            )
            if query.count() == 0:
                score_staff = ScoreStaff(from_dict=score_staff_mock)
                Wrapper.check_and_save(score_staff)
                print("CREATED score_staff")
                pprint(vars(score_staff))

        #BAR
        bars = []
        for bar_mock in bar_mocks:
            staff = staves[bar_mock['staffIndex']]
            query = Bar.query.filter_by(
                positionIndex=bar_mock['positionIndex'],
                staffId=staff.id
            )
            if query.count() == 0:
                bar = Bar(from_dict=bar_mock)
                bar.staff = staff
                Wrapper.check_and_save(bar)
                print("CREATED bar")
                pprint(vars(bar))
            else:
                bar = query.first()
            bars.append(bar)

        #VOICE
        voices = []
        for voice_mock in voice_mocks:
            melody = melodies[voice_mock['melodyIndex']]
            rhythm = rhythms[voice_mock['rhythmIndex']]
            query = Voice.query.filter_by(
                melodyId=melody.id,
                rhythmId=rhythm.id
            )
            if query.count() == 0:
                voice = Voice(from_dict=voice_mock)
                Wrapper.check_and_save(voice)
                print("CREATED voice")
                pprint(vars(voice))
            else:
                voice = query.first()
            voices.append(voice)


        #BAR VOICE
        for bar_voice_mock in bar_voice_mocks:
            bar = bars[bar_voice_mock['barIndex']]
            voice = voices[bar_voice_mock['voiceIndex']]
            query = BarVoice.query.filter_by(
                positionIndex=score_staff_mock['positionIndex'],
                barId=bar.id,
                voiceId=voice.id
            )
            if query.count() == 0:
                bar_voice = BarVoice(from_dict=bar_voice_mock)
                Wrapper.check_and_save(bar_voice)
                print("CREATED bar_voice")
                pprint(vars(bar_voice))
