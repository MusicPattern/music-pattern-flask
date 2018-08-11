""" voice """
from sqlalchemy import BigInteger,\
                       Column,\
                       ForeignKey,\
                       String
from sqlalchemy.orm import relationship

from models.utils import Model, Wrapper


class Voice(Wrapper,
            Model):

    name = Column(String(30))

    melodyId = Column(BigInteger,
                      ForeignKey("melody.id"),
                      nullable=True)

    melody = relationship('Melody',
                          foreign_keys=[melodyId],
                          backref='voices')

    rhythmId = Column(BigInteger,
                      ForeignKey("rhythm.id"),
                      nullable=True)

    rhythm = relationship('Rhythm',
                          foreign_keys=[rhythmId],
                          backref='voices')
