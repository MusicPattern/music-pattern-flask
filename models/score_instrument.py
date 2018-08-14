""" score instrument """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class ScoreInstrument(Wrapper,
                      Model):

    positionIndex = Column(BigInteger)

    scoreId = Column(BigInteger,
                     ForeignKey('score.id'),
                     primary_key=True)

    score = relationship('Score',
                         foreign_keys=[scoreId],
                         backref=backref("scoreInstruments"))

    instrumentId = Column(BigInteger,
                   ForeignKey('instrument.id'),
                   primary_key=True)

    instrument = relationship('Instrument',
                       foreign_keys=[instrumentId],
                       backref=backref("scoreInstruments"))
