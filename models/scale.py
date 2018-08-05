""" scale """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.db import Model
from models.wrapper import Wrapper


class Scale(Wrapper,
            Model,
            ):

    name = Column(String(30), nullable=False)
