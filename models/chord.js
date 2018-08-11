""" chord """
from sqlalchemy import BigInteger,\
                       Column,\
                       ForeignKey,\
                       String

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
