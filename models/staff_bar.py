""" staff bar """
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship

from models.utils import Model, Wrapper


class StaffBar(Wrapper,
               Model):

    positionIndex = Column(BigInteger)
    
    staffId = Column(BigInteger,
                     ForeignKey('staff.id'),
                     primary_key=True)

    staff = relationship('Staff',
                         foreign_keys=[staffId],
                         backref=backref("staffBars"))

    barId = Column(BigInteger,
                   ForeignKey('bar.id'),
                   primary_key=True)

    bar = relationship('Bar',
                       foreign_keys=[barId],
                       backref=backref("staffBars"))
