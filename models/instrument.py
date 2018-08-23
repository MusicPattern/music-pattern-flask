""" instrument """
from sqlalchemy import Column, String

from models.utils import Model, Wrapper


class Instrument(Wrapper,
                 Model):

    name = Column(String(100))

    toneName = Column(String(100))
