""" staff """
from itertools import combinations
from sqlalchemy import BigInteger,\
                       Column,\
                       String

from models.utils import Model, Wrapper


class Staff(Wrapper,
             Model):

    name = Column(String(30))

    clef = Column(BigInteger())

    keySignature = Column(BigInteger())
