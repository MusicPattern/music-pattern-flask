""" bar voice """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class BarVoice(Wrapper,
               Model):

    positionIndex = Column(BigInteger)

    barId = Column(BigInteger,
                   ForeignKey('bar.id'),
                   primary_key=True)

    bar = relationship('Bar',
                       foreign_keys=[barId],
                       backref=backref("barVoices"))

    voiceId = Column(BigInteger,
                     ForeignKey('voice.id'),
                     primary_key=True)

    voice = relationship('Voice',
                         foreign_keys=[voiceId],
                         backref=backref("barVoices"))
