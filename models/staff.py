""" staff """
from sqlalchemy import BigInteger,\
                       Column,\
                       ForeignKey,\
                       String
from sqlalchemy.orm import relationship

from models.utils import Model, Wrapper


class Staff(Wrapper,
            Model):

    name = Column(String(30))

    positionIndex = Column(BigInteger)

    scoreId = Column(BigInteger,
                     ForeignKey("score.id"))

    score = relationship('Score',
                         foreign_keys=[scoreId],
                         backref='score')


    """
    clefNoteId = Column(BigInteger,
                        ForeignKey("note.id"),
                        nullable=True)

    clefNote = relationship('Note',
                            foreign_keys=[clefNoteId],
                            backref='staves')
    """

    clef = Column(String(30))

    timeSignature = Column(String(30))
