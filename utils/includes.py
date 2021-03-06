""" includes """

USER_INCLUDES = [
    "-password",
    "roles"
]

HARMONY_INCLUDES = [
    {
        "key": "scales",
        "includes": [
            {
                "key": "scaleNotes",
                "resolve": lambda scale_note, filters: scale_note['note'],
                "includes": ["note"]
            }
        ]
    }
]

PATTERN_INCLUDES = [
    "melody",
    "rhythm"
]

STAFF_VOICE_INCLUDES = [
    {
        "key": "voice",
        "includes": [
            {
                "key": "voicePatterns",
                "includes": [
                    {
                        "key": "pattern",
                        "includes": PATTERN_INCLUDES
                    }
                ]

            }

        ]
    }
]

SCORE_INCLUDES = [
    {
        "key": "scoreInstruments",
        "includes": [
            {
                "key": "instrument",
                "includes": [
                    {
                        "key": "sounds",
                        "includes": [
                            "pitch",
                            "sample"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "key": "scoreStaves",
        "includes": [
            {
                "key": "staff",
                "includes": [
                    {
                        "key": "staffVoices",
                        "includes": STAFF_VOICE_INCLUDES
                    }
                ]
            }
        ]
    }
]
