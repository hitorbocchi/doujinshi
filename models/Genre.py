from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Genre(Base):

	__tablename__ = 'Genre'

	GenreId  = Column( Integer, primary_key=True, index=True )
	Version = Column( Integer )
	Name_EN = Column( String )
	Name_JP = Column( String )
	Name_R  = Column( String )
	Objects = Column( Integer )

	'''
	''
	'' Relationships
	''
	'''

	authors    = relationship('Author',    secondary='AuthorGenre',    back_populates='genres')
	books      = relationship('Book',      secondary='BookGenre',      back_populates='genres')
	characters = relationship('Character', secondary='CharacterGenre', back_populates='genres')
	circles    = relationship('Circle',    secondary='CircleGenre',    back_populates='genres')
	parodies   = relationship('Parody',    secondary='ParodyGenre',    back_populates='genres')
