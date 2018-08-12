""" includes """

USER_INCLUDES = [
    "-password",
    "roles"
]

HARMONY_INCLUDES = [
    {
        "key": "scales",
        "sub_joins": [
            {
                "key": "scaleNotes",
                "resolve": lambda scale_note, filters: scale_note['note'],
                "sub_joins": ["note"]
            }
        ]
    }
]

SCORE_INCLUDES = [
    {
        "key": "staves",
        "sub_joins": [
            
        ]
    }
]
