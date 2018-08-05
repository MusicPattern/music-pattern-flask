""" scale """
from sqlalchemy import BigInteger, Column, String

from models.db import Model
from models.wrapper import Wrapper


class Scale(Wrapper,
            Model):

    name = Column(String(30))

    size = Column(BigInteger())
