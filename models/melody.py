""" melody """
from sqlalchemy import Column,\
                       String

from models.utils import Model, Wrapper


class Melody(Wrapper,
             Model):

    pattern = Column(String(30))
