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
