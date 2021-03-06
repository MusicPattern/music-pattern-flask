""" note """
from sqlalchemy import BigInteger,\
                       Column,\
                       String

from models.utils import Model, Wrapper


class Note(Wrapper,
           Model):

    name = Column(String(30))

    index = Column(BigInteger,
                   unique=True)
