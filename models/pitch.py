""" pitch """
from sqlalchemy import BigInteger,\
                       Column,\
                       ForeignKey
from sqlalchemy.orm import relationship

from models.utils import Model, Wrapper


class Pitch(Wrapper,
            Model):

    index = Column(BigInteger,
                   unique=True)

    noteId = Column(BigInteger,
                    ForeignKey("note.id"),
                    nullable=True)

    note = relationship('Note',
                        foreign_keys=[noteId],
                        backref='pitches')
