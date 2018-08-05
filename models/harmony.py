""" harmony """
from sqlalchemy import BigInteger,\
                       Column,\
                       String

from models.db import Model
from models.wrapper import Wrapper


class Harmony(Wrapper,
              Model):

    name = Column(String(30))

    notesMax = Column(BigInteger())

    pitchesMax = Column(BigInteger())

    scaleMaxSize = Column(BigInteger())
