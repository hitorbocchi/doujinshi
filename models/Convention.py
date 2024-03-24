from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Convention(Base):

	__tablename__ = 'Convention'

	ConventionId  = Column( Integer, primary_key=True, index=True )
	Version       = Column( Integer )
	Name_EN       = Column( String )
	Name_JP       = Column( String )
	Name_R        = Column( String )
	Objects       = Column( Integer )
	Date_Start    = Column( Date )
	Date_End      = Column( Date )

	'''
	''
	'' Relationships
	''
	'''

	convention_character_table = Table( 'ConventionCharacter', Base.metadata,
		Column('ConventionId', Integer, ForeignKey('Convention.ConventionId'), primary_key=True ),
		Column('CharacterId',  Integer, ForeignKey('Character.CharacterId'),   primary_key=True ),
	)

	convention_content_table = Table( 'ConventionContent', Base.metadata,
		Column('ConventionId', Integer, ForeignKey('Convention.ConventionId'), primary_key=True ),
		Column('ContentId',    Integer, ForeignKey('Content.ContentId'),       primary_key=True ),
	)

	convention_parody_table = Table( 'ConventionParody', Base.metadata,
		Column('ConventionId', Integer, ForeignKey('Convention.ConventionId'), primary_key=True ),
		Column('ParodyId',     Integer, ForeignKey('Parody.ParodyId'),   primary_key=True ),
	)

	books      = relationship('Book',      secondary='BookConvention',           back_populates='conventions')
	characters = relationship('Character', secondary=convention_character_table, back_populates='conventions')
	contents   = relationship('Content',   secondary=convention_content_table,   back_populates='conventions')
	parodies   = relationship('Parody',    secondary=convention_parody_table,    back_populates='conventions')