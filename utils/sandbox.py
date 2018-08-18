""" sandbox """
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# -*- coding: utf-8 -*-
from pprint import pprint

from mock.scripts import harmony_mocks,\
                         instrument_mocks,\
                         melody_mocks,\
                         pattern_mocks,\
                         sample_mocks,\
                         score_mocks,\
                         score_instrument_mocks,\
                         score_staff_mocks,\
                         staff_mocks,\
                         staff_voice_mocks,\
                         sound_mocks,\
                         rhythm_mocks,\
                         user_mocks,\
                         voice_mocks,\
                         voice_pattern_mocks
from models.utils import Wrapper
from models import Harmony,\
                   Instrument,\
                   Sound,\
                   Melody,\
                   Note,\
                   Pattern,\
                   Pitch,\
                   Rhythm,\
                   Role,\
                   Sample,\
                   Scale,\
                   ScaleNote,\
                   Score,\
                   ScoreInstrument,\
                   ScoreStaff,\
                   Sound,\
                   Staff,\
                   StaffVoice,\
                   User,\
                   Voice,\
                   VoicePattern

from utils.mock import set_from_mock


def do_sandbox():

    #USER
    users_by_email = {}
    for (user_index, user_mock) in enumerate(user_mocks):
        query = User.query.filter_by(email=user_mock['email'])
        if query.count() == 0:
            user = User(from_dict=user_mock)
            user.validationToken = None
            Wrapper.check_and_save(user)
            set_from_mock("thumbs", user, user_index)
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
        users_by_email[user.email] = user

    #SAMPLE
    samples_by_name = {}
    for (sample_index, sample_mock) in enumerate(sample_mocks):
        query = Sample.query.filter_by(name=sample_mock['name'])
        if query.count() == 0:
            sample = Sample(from_dict=sample_mock)
            Wrapper.check_and_save(sample)
            set_from_mock("audios", sample, sample_index)
            print("CREATED sample")
            pprint(vars(sample))
        else:
            sample = query.first()
        samples_by_name[sample.name] = sample

    #INSTRUMENT
    instruments_by_name = {}
    for (instrument_index, instrument_mock) in enumerate(instrument_mocks):
        query = Instrument.query.filter_by(name=instrument_mock['name'])
        if query.count() == 0:
            instrument = Instrument(from_dict=instrument_mock)
            Wrapper.check_and_save(instrument)
            print("CREATED instrument")
            pprint(vars(instrument))
        else:
            instrument = query.first()
        instruments_by_name[instrument.name] = instrument

    #HARMONY
    harmonies_by_name = {}
    for (harmony_index, harmony_mock) in enumerate(harmony_mocks):
        query = Harmony.query.filter_by(name=harmony_mock['name'])
        if query.count() == 0:
            harmony = Harmony(from_dict=harmony_mock)
            Wrapper.check_and_save(harmony)
            print("CREATED harmony")
            pprint(vars(harmony))
        else:
            harmony = query.first()
        harmonies_by_name[harmony.name] = harmony

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
        pitches = []
        for index in range(harmony.pitchesMax):
            query = Pitch.query.filter_by(index=index)
            if query.count() == 0:
                pitch = Pitch(from_dict={ "index": index })
                pitch.note = notes[note_index]
                Wrapper.check_and_save(pitch)
                print("CREATED pitch")
                pprint(vars(pitch))
            else:
                pitch = query.first()
            pitches.append(pitch)
            note_index += 1
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

    #SOUND
    for sound_mock in sound_mocks:
        instrument = instruments_by_name[sound_mock['instrumentName']]
        pitch = pitches[sound_mock['pitchIndex']]
        sample = samples_by_name[sound_mock['sampleName']]
        query = Sound.query.filter_by(
            instrumentId=instrument.id,
            pitchId=pitch.id,
            sampleId=sample.id
        )
        if query.count() == 0:
            sound = Sound(from_dict=sound_mock)
            sound.instrument = instrument
            sound.pitch = pitch
            sound.sample = sample
            Wrapper.check_and_save(sound)
            print("CREATED sound")
            pprint(vars(sound))

    #MELODY
    melodies_by_name = {}
    for melody_mock in melody_mocks:
        query = Melody.query.filter_by(name=melody_mock['name'])
        if query.count() == 0:
            melody = Melody(from_dict=melody_mock)
            Wrapper.check_and_save(melody)
            print("CREATED melody")
            pprint(vars(melody))
        else:
            melody = query.first()
        melodies_by_name[melody.name] = melody

    #RHYTHM
    rhythms_by_name = {}
    for rhythm_mock in rhythm_mocks:
        query = Rhythm.query.filter_by(name=rhythm_mock['name'])
        if query.count() == 0:
            rhythm = Rhythm(from_dict=rhythm_mock)
            Wrapper.check_and_save(rhythm)
            print("CREATED rhythm")
            pprint(vars(rhythm))
        else:
            rhythm = query.first()
        rhythms_by_name[rhythm.name] = rhythm

    #PATTERN
    patterns_by_name = {}
    for pattern_mock in pattern_mocks:
        melody = melodies_by_name[pattern_mock['melodyName']]
        rhythm = rhythms_by_name[pattern_mock['rhythmName']]
        query = Pattern.query.filter_by(
            melodyId=melody.id,
            rhythmId=rhythm.id
        )
        if query.count() == 0:
            pattern = Pattern(from_dict=pattern_mock)
            pattern.melody = melody
            pattern.rhythm = rhythm
            Wrapper.check_and_save(pattern)
            print("CREATED pattern")
            pprint(vars(pattern))
        else:
            pattern = query.first()
        patterns_by_name[pattern.name] = pattern


    #SCORE
    scores_by_name = {}
    for score_mock in score_mocks:
        query = Score.query.filter_by(name=score_mock['name'])
        if query.count() == 0:
            score = Score(from_dict=score_mock)
            user = users_by_email[score_mock['userEmail']]
            score.user = user
            Wrapper.check_and_save(score)
            print("CREATED score")
            pprint(vars(score))
        else:
            score = query.first()
        scores_by_name[score.name] = score

    #STAFF
    staves_by_name = {}
    for staff_mock in staff_mocks:
        query = Staff.query.filter_by(
            name=staff_mock['name']
        )
        if query.count() == 0:
            staff = Staff(from_dict=staff_mock)
            Wrapper.check_and_save(staff)
            print("CREATED staff")
            pprint(vars(staff))
        else:
            staff = query.first()
        staves_by_name[staff.name] = staff

    #SCORE STAFF
    for score_staff_mock in score_staff_mocks:
        score = scores_by_name[score_staff_mock['scoreName']]
        staff = staves_by_name[score_staff_mock['staffName']]
        query = ScoreStaff.query.filter_by(
            positionIndex=score_staff_mock['positionIndex'],
            scoreId=score.id,
            staffId=staff.id
        )
        if query.count() == 0:
            score_staff = ScoreStaff(from_dict=score_staff_mock)
            score_staff.score = score
            score_staff.staff = staff
            Wrapper.check_and_save(score_staff)
            print("CREATED score_staff")
            pprint(vars(score_staff))

    #SCORE INSTRUMENT
    for score_instrument_mock in score_instrument_mocks:
        score = scores_by_name[score_instrument_mock['scoreName']]
        instrument = instruments_by_name[score_instrument_mock['instrumentName']]
        query = ScoreInstrument.query.filter_by(
            positionIndex=score_instrument_mock['positionIndex'],
            scoreId=score.id,
            instrumentId=instrument.id
        )
        if query.count() == 0:
            score_instrument = ScoreInstrument(from_dict=score_instrument_mock)
            score_instrument.score = score
            score_instrument.instrument = instrument
            Wrapper.check_and_save(score_instrument)
            print("CREATED score_instrument")
            pprint(vars(score_instrument))

    #VOICE
    voices_by_name = {}
    for voice_mock in voice_mocks:
        query = Voice.query.filter_by(name=voice_mock['name'])
        if query.count() == 0:
            voice = Voice(from_dict=voice_mock)
            Wrapper.check_and_save(voice)
            print("CREATED voice")
            pprint(vars(voice))
        else:
            voice = query.first()
        voices_by_name[voice.name] = voice

    #VOICE PATTERNS
    for voice_pattern_mock in voice_pattern_mocks:
        voice = voices_by_name[voice_pattern_mock['voiceName']]
        pattern = patterns_by_name[voice_pattern_mock['patternName']]
        query = VoicePattern.query.filter_by(
            voiceId=voice.id,
            patternId=pattern.id
        )
        if query.count() == 0:
            voice_pattern = VoicePattern(from_dict=voice_pattern_mock)
            voice_pattern.voice = voice
            voice_pattern.pattern = pattern
            Wrapper.check_and_save(voice_pattern)
            print("CREATED voice_pattern")
            pprint(vars(voice_pattern))


    #STAFF VOICE
    for staff_voice_mock in staff_voice_mocks:
        staff = staves_by_name[staff_voice_mock['staffName']]
        voice = voices_by_name[staff_voice_mock['voiceName']]
        query = StaffVoice.query.filter_by(
            staffId=staff.id,
            voiceId=voice.id
        )
        if query.count() == 0:
            staff_voice = StaffVoice(from_dict=staff_voice_mock)
            staff_voice.staff = staff
            staff_voice.voice = voice
            Wrapper.check_and_save(staff_voice)
            print("CREATED staff_voice")
            pprint(vars(staff_voice))
