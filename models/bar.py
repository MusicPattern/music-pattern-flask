""" bar """
from sqlalchemy import Column,\
                       String

from models.utils import Model, Wrapper


class Bar(Wrapper,
          Model):

    name = Column(String(30))
