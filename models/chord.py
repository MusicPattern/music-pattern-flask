""" chord """
from sqlalchemy import BigInteger,\
                       Column,\
                       ForeignKey,\
                       String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from models.utils import Model, Wrapper


class Chord(Wrapper,
            Model):

    name = Column(String(30))

    harmonyId = Column(BigInteger,
                       ForeignKey("harmony.id"),
                       nullable=True)

    harmony = relationship('Harmony',
                           foreign_keys=[harmonyId],
                           backref='chords')


    tags = Column(ARRAY(String(220)),
                  nullable=False,
                  default=[])
