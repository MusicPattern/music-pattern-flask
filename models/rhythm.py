""" rhythm """
from sqlalchemy import Column,\
                       String

from models.utils import Model, Wrapper


class Rhythm(Wrapper,
             Model):

    name = Column(String())

    durations = Column(String())
