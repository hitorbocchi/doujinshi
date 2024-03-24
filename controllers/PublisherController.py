from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Publisher import Publisher
from schemas import PublisherBase, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Publisher Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ PublisherBase ]:
	return paginate_query( db, select(Publisher).order_by( Publisher.PublisherId ) )

@router.get('/{publisherId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, publisherId: int = Path( gt=0 ) ) -> PublisherBase:
	publisher = db.query(Publisher).filter( Publisher.PublisherId == publisherId ).first()

	if publisher is not None:
		return publisher
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{publisherId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, publisherId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	publisher = db.query(Publisher).filter( Publisher.PublisherId == publisherId ).first()

	if publisher is not None:
		return paginate( publisher.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")