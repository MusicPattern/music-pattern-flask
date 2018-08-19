""" sound sample """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class Sound(Wrapper,
            Model):

    instrumentId = Column(BigInteger,
                          ForeignKey('instrument.id'),
                          primary_key=True)

    instrument = relationship('Instrument',
                              foreign_keys=[instrumentId],
                              backref=backref("sounds"))

    """
    pitchId = Column(BigInteger,
                     ForeignKey('pitch.id'),
                     primary_key=True)

    pitch = relationship('Pitch',
                         foreign_keys=[pitchId],
                         backref=backref("sounds"))
    """

    pitch = Column(BigInteger)

    sampleId = Column(BigInteger,
                      ForeignKey('sample.id'),
                      primary_key=True)

    sample = relationship('Sample',
                          foreign_keys=[sampleId],
                          backref=backref("sounds"))
