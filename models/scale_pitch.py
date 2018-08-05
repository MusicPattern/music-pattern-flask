""" scale pitch """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.db import Model
from models.wrapper import Wrapper


class ScalePitch(Wrapper,
                 Model):

    scaleId = Column(BigInteger,
                     ForeignKey('scale.id'),
                     primary_key=True)

    scale = relationship('Scale',
                         foreign_keys=[scaleId],
                         backref=backref("scalePitches"))

    pitchId = Column(BigInteger,
                     ForeignKey('pitch.id'),
                     primary_key=True)

    pitch = relationship('Pitch',
                         foreign_keys=[pitchId],
                         backref=backref("scalePitches"))
