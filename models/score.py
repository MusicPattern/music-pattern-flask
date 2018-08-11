""" score """
from sqlalchemy import BigInteger,\
                       Column,\
                       String

from models.utils import Model, Wrapper

class Score(Wrapper,
            Model):

    name = Column(String(30))

    clef = Column(BigInteger())

    keySignature = Column(BigInteger())
