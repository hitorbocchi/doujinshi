from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Parody(Base):

	__tablename__ = 'Parody'

	ParodyId = Column( Integer, primary_key=True, index=True )
	Version  = Column( Integer )
	Name_EN  = Column( String )
	Name_JP  = Column( String )
	Name_R   = Column( String )
	Objects  = Column( Integer )
	TypeId   = Column( Integer )

	'''
	''
	'' Relationships
	''
	'''

	parody_character_table = Table( 'ParodyCharacter', Base.metadata,
		Column('ParodyId',    Integer, ForeignKey('Parody.ParodyId'),       primary_key=True ),
		Column('CharacterId', Integer, ForeignKey('Character.CharacterId'), primary_key=True ),
	)

	parody_content_table = Table( 'ParodyContent', Base.metadata,
		Column('ParodyId',   Integer, ForeignKey('Parody.ParodyId'),     primary_key=True ),
		Column('ContentId', Integer, ForeignKey('Content.ContentId'), primary_key=True ),
	)

	parody_genre_table = Table( 'ParodyGenre', Base.metadata,
		Column('ParodyId',   Integer, ForeignKey('Parody.ParodyId'),     primary_key=True ),
		Column('GenreId', Integer, ForeignKey('Genre.GenreId'), primary_key=True ),
	)

	books       = relationship('Book',       secondary='BookParody',           back_populates='parodies')
	characters  = relationship('Character',  secondary=parody_character_table, back_populates='parodies')
	conventions = relationship('Convention', secondary='ConventionParody',     back_populates='parodies')
	contents    = relationship('Content',    secondary=parody_content_table,   back_populates='parodies')
	genres      = relationship('Genre',      secondary=parody_genre_table,     back_populates='parodies')