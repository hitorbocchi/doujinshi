from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Author(Base):

	__tablename__ = 'Author'

	AuthorId = Column( Integer, primary_key=True, index=True )
	Version  = Column( Integer )
	Parent   = Column( Integer )
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

	author_content_table = Table( 'AuthorContent', Base.metadata,
		Column('AuthorId',  Integer, ForeignKey('Author.AuthorId'),   primary_key=True ),
		Column('ContentId', Integer, ForeignKey('Content.ContentId'), primary_key=True ),
	)

	author_genre_table = Table( 'AuthorGenre', Base.metadata,
		Column('AuthorId', Integer, ForeignKey('Author.AuthorId'), primary_key=True ),
		Column('GenreId',  Integer, ForeignKey('Genre.GenreId'),   primary_key=True ),
	)

	books    = relationship('Book',    secondary='BookAuthor',         back_populates='authors')
	circles  = relationship('Circle',  secondary='CircleAuthor',       back_populates='authors')
	contents = relationship('Content', secondary=author_content_table, back_populates='authors')
	genres   = relationship('Genre',   secondary=author_genre_table,   back_populates='authors')
