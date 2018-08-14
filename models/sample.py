""" sample """
from sqlalchemy import Column, String

from models.mixins import HasAudioMixin
from models.utils import Model, Wrapper


class Sample(Wrapper,
             Model,
             HasAudioMixin):

    name = Column(String())
