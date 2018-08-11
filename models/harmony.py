""" harmony """
from itertools import combinations
from sqlalchemy import BigInteger,\
                       Column,\
                       String

from models.utils import Model, Wrapper


class Harmony(Wrapper,
              Model):

    name = Column(String(30))

    notesMax = Column(BigInteger())

    pitchesMax = Column(BigInteger())

    scaleMaxSize = Column(BigInteger())

    def get_scale_note_indexes_combinations(self, scale_size = 3):
        harmony = Harmony.query.filter_by(name=self.name).first()

        return [
            tuple([0] + list(c))
            for c in combinations(range(1, harmony.notesMax), scale_size - 1)
        ]
