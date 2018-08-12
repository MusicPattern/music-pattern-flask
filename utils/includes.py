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
        "key": "staves",
        "includes": [
            {
                "key": "staffBars",
                "resolve": lambda staff_bar, filters: staff_bar['bar'],
                "includes": [
                    {
                        "key": "voices",
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
