""" chord note """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class ChordNote(Wrapper,
                Model):

    chordId = Column(BigInteger,
                     ForeignKey('chord.id'),
                     primary_key=True)

    chord = relationship('Chord',
                         foreign_keys=[chordId],
                         backref="chordNotes")

    noteId = Column(BigInteger,
                    ForeignKey('note.id'),
                    primary_key=True)

    note = relationship('Note',
                        foreign_keys=[noteId],
                        backref="chordNotes")
