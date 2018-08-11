""" bar """
from sqlalchemy import BigInteger,\
                       Column,\
                       ForeignKey,\
                       String
from sqlalchemy.orm import relationship

from models.utils import Model, Wrapper


class Bar(Wrapper,
          Model):

    name = Column(String(30))

    staffId = Column(BigInteger,
                     ForeignKey("staff.id"),
                     nullable=True)

    staff = relationship('Staff',
                         foreign_keys=[staffId],
                         backref='bars')
