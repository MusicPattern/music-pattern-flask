""" harmony """
from sqlalchemy import BigInteger,\
                       Column,\
                       String

from models.db import Model
from models.wrapper import Wrapper


class Harmony(Wrapper,
              Model):

    name = Column(String(30))

    notesMaxLength = Column(BigInteger())

    pitchesMaxLength = Column(BigInteger())

    scalesMaxLength = Column(BigInteger())
