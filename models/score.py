""" score """
from sqlalchemy import Column,\
                       String

from models.utils import Model, Wrapper

class Score(Wrapper,
            Model):

    name = Column(String(30))
