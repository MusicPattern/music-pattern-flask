""" role """
import enum
from sqlalchemy import BigInteger,\
                       Column,\
                       ForeignKey,\
                       String
from sqlalchemy.orm import relationship

from models.db import Model
from models.wrapper import Wrapper

class RoleType(enum.Enum):
    admin = "admin"
    editor = "editor"
    reviewer = "reviewer"

class Role(Wrapper,
           Model):

    userId = Column(BigInteger,
                    ForeignKey('user.id'),
                    nullable=False,
                    index=True)

    user = relationship('User',
                        foreign_keys=[userId],
                        backref='roles')

    type = Column(String(50),
                  nullable=True)
