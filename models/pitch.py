""" pitch """
from sqlalchemy import BigInteger,\
                       Column

from models.db import Model
from models.wrapper import Wrapper


class Pitch(Wrapper,
            Model):

    index = Column(BigInteger,
                   unique=True)
