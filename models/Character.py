from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Character(Base):

	__tablename__ = 'Character'

	CharacterId = Column( Integer, primary_key=True, index=True )
	Version     = Column( Integer )
	Name_EN     = Column( String )
	Name_JP     = Column( String )
	Name_R      = Column( String )
	Objects     = Column( Integer )
	Sex         = Column( Integer )
	Age         = Column( Integer )

	'''
	''
	'' Relationships
	''
	'''

	character_content_table = Table( 'CharacterContent', Base.metadata,
		Column('CharacterId', Integer, ForeignKey('Character.CharacterId'), primary_key=True ),
		Column('ContentId',   Integer, ForeignKey('Content.ContentId'),     primary_key=True ),
	)

	character_genre_table = Table( 'CharacterGenre', Base.metadata,
		Column('CharacterId', Integer, ForeignKey('Character.CharacterId'), primary_key=True ),
		Column('GenreId',     Integer, ForeignKey('Genre.GenreId'),         primary_key=True ),
	)

	books       = relationship('Book',       secondary='BookCharacter',         back_populates='characters')
	contents    = relationship('Content',    secondary=character_content_table, back_populates='characters')
	genres      = relationship('Genre',      secondary=character_genre_table,   back_populates='characters')
	conventions = relationship('Convention', secondary='ConventionCharacter',   back_populates='characters')
	parodies    = relationship('Parody',     secondary='ParodyCharacter',       back_populates='characters')
