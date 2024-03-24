from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Genre import Genre
from schemas import GenreBase, GenreDetail, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Genre Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ GenreBase ]:
	return paginate_query( db, select(Genre).order_by( Genre.GenreId ) )

@router.get('/{genreId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, genreId: int = Path( gt=0 ) ) -> GenreDetail:
	genre = db.query(Genre).filter( Genre.GenreId == genreId ).first()

	if genre is not None:
		return genre
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{genreId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, genreId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	genre = db.query(Genre).filter( Genre.GenreId == genreId ).first()

	if genre is not None:
		return paginate( genre.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")