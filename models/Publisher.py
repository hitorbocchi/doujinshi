from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.database import Base

class Publisher(Base):

	__tablename__ = 'Publisher'

	PublisherId = Column( Integer, primary_key=True, index=True )
	Version     = Column( Integer )
	Name_EN     = Column( String )
	Name_JP     = Column( String )
	Name_R      = Column( String )
	Objects     = Column( Integer )

	'''
	''
	'' Relationships
	''
	'''
	
	books = relationship('Book', back_populates='publisher')