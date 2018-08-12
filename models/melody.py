""" melody """
from sqlalchemy import Column,\
                       String

from models.utils import Model, Wrapper


class Melody(Wrapper,
             Model):

    name = Column(String(30))
    
    pattern = Column(String(30))
