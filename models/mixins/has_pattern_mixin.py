from sqlalchemy import Column,\
                       ForeignKey,\
                       String

class HasPatternMixin(object):

    harmonyId = Column(BigInteger,
                       ForeignKey("harmony.id"),
                       nullable=True)

    harmony = relationship('Harmony',
                           foreign_keys=[harmonyId],
                           backref='scales')

    name = Column(String(30))

    pattern = Column(String(30))

    size = Column(BigInteger())

    tags = Column(ARRAY(String(220)),
                  nullable=False,
                  default=[])
