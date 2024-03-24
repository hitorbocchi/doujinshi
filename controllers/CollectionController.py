from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Collection import Collection
from schemas import CollectionBase, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Collection Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ CollectionBase ]:
	return paginate_query( db, select(Collection).order_by( Collection.CollectionId ) )

@router.get('/{collectionId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, collectionId: int = Path( gt=0 ) ) -> CollectionBase:
	collection = db.query(Collection).filter( Collection.CollectionId == collectionId ).first()

	if collection is not None:
		return collection
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{collectionId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, collectionId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	collection = db.query(Collection).filter( Collection.CollectionId == collectionId ).first()

	if collection is not None:
		return paginate( collection.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")