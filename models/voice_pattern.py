""" voice pattern """
from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class VoicePattern(Wrapper,
                   Model):

    positionIndex = Column(BigInteger)

    probabilities = Column(String())

    rootInterval = Column(BigInteger)

    rootDuration = Column(BigInteger)

    voiceId = Column(BigInteger,
                     ForeignKey('voice.id'),
                     primary_key=True)

    voice = relationship('Voice',
                         foreign_keys=[voiceId],
                         backref=backref("voicePatterns"))

    patternId = Column(BigInteger,
                       ForeignKey('pattern.id'),
                       primary_key=True)

    pattern = relationship('Pattern',
                           foreign_keys=[patternId],
                           backref=backref("voicePatterns"))
