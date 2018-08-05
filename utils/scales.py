""" harmony """
from itertools import combinations

from models.harmony import Harmony

def get_scale_note_indexes_combinations(scale_size = 3, harmony_name="chromatic"):
    harmony = Harmony.query.filter_by(name=harmony_name).first()

    return [
        tuple([0] + list(c))
        for c in combinations(range(1, harmony.notesMax), scale_size - 1)
    ]
