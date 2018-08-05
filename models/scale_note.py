""" scale note """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.db import Model
from models.wrapper import Wrapper


class ScaleNote(Wrapper,
                Model):

    scaleId = Column(BigInteger,
                     ForeignKey('scale.id'),
                     primary_key=True)

    scale = relationship('Scale',
                         foreign_keys=[scaleId],
                         backref=backref("scaleNotes"))

    noteId = Column(BigInteger,
                    ForeignKey('note.id'),
                    primary_key=True)

    note = relationship('Note',
                        foreign_keys=[noteId],
                        backref=backref("scaleNotes"))
