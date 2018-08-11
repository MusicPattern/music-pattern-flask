""" harmonies """
from music.chromatic_scale import get_chromatic_scale_name, get_chromatic_scale_tags

harmony_mocks = [
    {
        "get_scale_name": get_chromatic_scale_name,
        "get_scale_tags": get_chromatic_scale_tags,
        "name": "chromatic",
        "noteNames": [
            "C",     #0
            "C#/Db", #1
            "D",     #2
            "D#/Eb", #3
            "E",     #4
            "F",     #5
            "F#/Gb", #6
            "G",     #7
            "G#/Ab", #8
            "A",     #9
            "A#/Bb", #10
            "B"      #11
        ],
        "notesMax": 12,
        "pitchesMax": 12 * 20,
        "scaleMaxSize": 8
    }
]
