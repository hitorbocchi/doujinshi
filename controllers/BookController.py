from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Book import Book
from schemas import BookCatalog, BookDetail

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Book Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ BookCatalog ]:
	return paginate_query( db, select(Book).order_by( Book.BookId ) )

@router.get('/{bookId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, bookId: int = Path( gt=0 ) ) -> BookDetail:
	book = db.query(Book).filter( Book.BookId == bookId ).first()

	if book is not None:
		return book
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")