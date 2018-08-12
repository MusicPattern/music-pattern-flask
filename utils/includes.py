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

SCORE_INCLUDES = [
    {
        "key": "scoreStaves",
        "resolve": lambda score_staff, filters: score_staff['staff'],
        "includes": [
            {
                "key": "staff",
                "includes": [
                    {
                        "key": "staffBars",
                        "resolve": lambda staff_bar, filters: staff_bar['bar'],
                        "includes": [
                            {
                                "key": "bar",
                                "includes": [
                                    {
                                        "key": "barVoices",
                                        "resolve": lambda bar_voice, filters: bar_voice['voice'],
                                        "includes": [
                                            {
                                                "key": "voice",
                                                "includes": [
                                                    "melody",
                                                    "rhythm"
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
