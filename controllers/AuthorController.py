from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Author import Author
from schemas import AuthorBase, AuthorDetail, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Author Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ AuthorBase ]:
	return paginate_query( db, select(Author).order_by( Author.AuthorId ) )

@router.get('/{authorId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, authorId: int = Path( gt=0 ) ) -> AuthorDetail:
	author = db.query(Author).filter( Author.AuthorId == authorId ).first()

	if author is not None:
		return author
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{authorId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, authorId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	author = db.query(Author).filter( Author.AuthorId == authorId ).first()

	if author is not None:
		return paginate( author.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")