from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Content(Base):

	__tablename__ = 'Content'

	ContentId = Column( Integer, primary_key=True, index=True )
	Version   = Column( Integer )
	Name_EN   = Column( String )
	Name_JP   = Column( String )
	Name_R    = Column( String )
	Objects   = Column( Integer )

	'''
	''
	'' Relationships
	''
	'''
	
	authors     = relationship('Author',     secondary='AuthorContent',     back_populates='contents')
	books       = relationship('Book',       secondary='BookContent',       back_populates='contents')
	characters  = relationship('Character',  secondary='CharacterContent',  back_populates='contents')
	circles     = relationship('Circle',     secondary='CircleContent',     back_populates='contents')
	conventions = relationship('Convention', secondary='ConventionContent', back_populates='contents')
	parodies    = relationship('Parody',     secondary='ParodyContent',     back_populates='contents')
	