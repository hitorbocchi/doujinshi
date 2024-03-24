from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Book(Base):

	__tablename__ = 'Book'

	BookId       = Column( Integer, primary_key=True, index=True )
	Version      = Column( Integer )
	Name_EN      = Column( String )
	Name_JP      = Column( String )
	Name_R       = Column( String )
	Released     = Column( Date )
	ISBN         = Column( Integer )
	Pages        = Column( Integer )
	Age          = Column( Integer )
	Anthology    = Column( Integer )
	Language     = Column( Integer )
	Copyshi      = Column( Integer )
	Magazine     = Column( Integer )
	Info         = Column( String )
	PublisherId  = Column( Integer, ForeignKey( 'Publisher.PublisherId' ) )
	CollectionId = Column( Integer, ForeignKey( 'Collection.CollectionId' ) )

	'''
	''
	'' Relationships
	''
	'''

	book_author_table = Table( 'BookAuthor', Base.metadata,
		Column('BookId',   Integer, ForeignKey('Book.BookId'),     primary_key=True ),
		Column('AuthorId', Integer, ForeignKey('Author.AuthorId'), primary_key=True ),
	)

	book_character_table = Table( 'BookCharacter', Base.metadata,
		Column('BookId',      Integer, ForeignKey('Book.BookId'),           primary_key=True ),
		Column('CharacterId', Integer, ForeignKey('Character.CharacterId'), primary_key=True ),
	)

	book_circle_table = Table( 'BookCircle', Base.metadata,
		Column('BookId',   Integer, ForeignKey('Book.BookId'),     primary_key=True ),
		Column('CircleId', Integer, ForeignKey('Circle.CircleId'), primary_key=True ),
	)

	book_content_table = Table( 'BookContent', Base.metadata,
		Column('BookId',    Integer, ForeignKey('Book.BookId'),       primary_key=True ),
		Column('ContentId', Integer, ForeignKey('Content.ContentId'), primary_key=True ),
	)

	book_convention_table = Table( 'BookConvention', Base.metadata,
		Column('BookId',       Integer, ForeignKey('Book.BookId'),             primary_key=True ),
		Column('ConventionId', Integer, ForeignKey('Convention.ConventionId'), primary_key=True ),
	)

	book_genre_table = Table( 'BookGenre', Base.metadata,
		Column('BookId',  Integer, ForeignKey('Book.BookId'),   primary_key=True ),
		Column('GenreId', Integer, ForeignKey('Genre.GenreId'), primary_key=True ),
	)

	book_imprint_table = Table( 'BookImprint', Base.metadata,
		Column('BookId',    Integer, ForeignKey('Book.BookId'),       primary_key=True ),
		Column('ImprintId', Integer, ForeignKey('Imprint.ImprintId'), primary_key=True ),
	)

	book_parody_table = Table( 'BookParody', Base.metadata,
		Column('BookId',   Integer, ForeignKey('Book.BookId'),     primary_key=True ),
		Column('ParodyId', Integer, ForeignKey('Parody.ParodyId'), primary_key=True ),
	)

	book_type_table = Table( 'BookType', Base.metadata,
		Column('BookId', Integer, ForeignKey('Book.BookId'), primary_key=True ),
		Column('TypeId', Integer, ForeignKey('Type.TypeId'), primary_key=True ),
	)

	authors      = relationship('Author',     secondary=book_author_table,     back_populates='books')
	characters   = relationship('Character',  secondary=book_character_table,  back_populates='books')
	circles      = relationship('Circle',     secondary=book_circle_table,     back_populates='books')
	collection   = relationship('Collection', back_populates='books')
	contents     = relationship('Content',    secondary=book_content_table,    back_populates='books')
	conventions  = relationship('Convention', secondary=book_convention_table, back_populates='books')
	genres       = relationship('Genre',      secondary=book_genre_table,      back_populates='books')
	imprints     = relationship('Imprint',    secondary=book_imprint_table,    back_populates='books')
	parodies     = relationship('Parody',     secondary=book_parody_table,     back_populates='books')
	publisher   = relationship('Publisher',   back_populates='books')
	types        = relationship('Type',       secondary=book_type_table,       back_populates='books')
