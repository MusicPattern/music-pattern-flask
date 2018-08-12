""" score staff """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class ScoreStaff(Wrapper,
                 Model):

    positionIndex = Column(BigInteger)

    scoreId = Column(BigInteger,
                     ForeignKey('score.id'),
                     primary_key=True)

    score = relationship('Score',
                         foreign_keys=[scoreId],
                         backref=backref("scoreStaves"))

    staffId = Column(BigInteger,
                     ForeignKey('staff.id'),
                     primary_key=True)

    staff = relationship('Staff',
                         foreign_keys=[staffId],
                         backref=backref("scoreStaves"))
