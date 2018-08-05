""" harmony """
from itertools import combinations, product

from models.harmony import Harmony

def get_scale_note_indexes(scale_size = 3, harmony=None):
    if harmony is None:
        harmony = Harmony.query.filter_by(name="chromatic")

    return [
        tuple([0] + list(c))
        for c in combinations(range(1, harmony.notesMaxLength), scale_size - 1)
    ]

print(get_scale_note_indexes(3))
