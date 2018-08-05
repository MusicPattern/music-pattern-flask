""" note """
from sqlalchemy import BigInteger,\
                       Column

from models.db import Model
from models.wrapper import Wrapper


class Note(Wrapper,
           Model):

    index = Column(BigInteger,
                   unique=True)
