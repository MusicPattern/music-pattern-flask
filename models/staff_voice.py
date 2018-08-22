""" staff voice """
from sqlalchemy import BigInteger, Boolean, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class StaffVoice(Wrapper,
                 Model):

    isActive = Column(Boolean,
                      nullable=False,
                      default=True)

    positionIndex = Column(BigInteger)

    staffId = Column(BigInteger,
                     ForeignKey('staff.id'),
                     primary_key=True)

    staff = relationship('Staff',
                         foreign_keys=[staffId],
                         backref=backref("staffVoices"))

    voiceId = Column(BigInteger,
                     ForeignKey('voice.id'),
                     primary_key=True)

    voice = relationship('Voice',
                         foreign_keys=[voiceId],
                         backref=backref("staffVoices"))
