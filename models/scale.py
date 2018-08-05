""" scale """
from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.db import Model
from models.wrapper import Wrapper


class Scale(Wrapper,
            Model):

    combinationIndex = Column(BigInteger())

    harmonyId = Column(BigInteger,
                       ForeignKey("harmony.id"),
                       nullable=True)

    harmony = relationship('Harmony',
                           foreign_keys=[harmonyId],
                           backref='scales')

    name = Column(String(30))

    size = Column(BigInteger())
