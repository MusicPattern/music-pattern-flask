""" staff """
from sqlalchemy import BigInteger,\
                       Column,\
                       String

from models.utils import Model, Wrapper


class Staff(Wrapper,
            Model):

    name = Column(String(30))

    clef = Column(String(30))

    timeSignature = Column(String(30))
