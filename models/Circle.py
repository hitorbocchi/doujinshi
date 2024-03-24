from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Circle(Base):

	__tablename__ = 'Circle'

	CircleId = Column( Integer, primary_key=True, index=True )
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
	
	circle_author_table = Table(
		'CircleAuthor', Base.metadata,
		Column('CircleId', Integer, ForeignKey('Circle.CircleId'), primary_key=True ),
		Column('AuthorId', Integer, ForeignKey('Author.AuthorId'), primary_key=True ),
	)

	circle_content_table = Table( 'CircleContent', Base.metadata,
		Column('CircleId',  Integer, ForeignKey('Circle.CircleId'),   primary_key=True ),
		Column('ContentId', Integer, ForeignKey('Content.ContentId'), primary_key=True ),
	)

	circle_genre_table = Table( 'CircleGenre', Base.metadata,
		Column('CircleId', Integer, ForeignKey('Circle.CircleId'), primary_key=True ),
		Column('GenreId',  Integer, ForeignKey('Genre.GenreId'),   primary_key=True ),
	)

	authors  = relationship('Author',  secondary=circle_author_table,  back_populates='circles')
	books    = relationship('Book',    secondary='BookCircle',         back_populates='circles')
	contents = relationship('Content', secondary=circle_content_table, back_populates='circles')
	genres   = relationship('Genre',   secondary=circle_genre_table,   back_populates='circles')