from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Circle import Circle
from schemas import CircleBase, CircleDetail, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Circle Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ CircleBase ]:
	return paginate_query( db, select(Circle).order_by( Circle.CircleId ) )

@router.get('/{circleId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, circleId: int = Path( gt=0 ) ) -> CircleDetail:
	circle = db.query(Circle).filter( Circle.CircleId == circleId ).first()

	if circle is not None:
		return circle
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{circleId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, circleId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	circle = db.query(Circle).filter( Circle.CircleId == circleId ).first()

	if circle is not None:
		return paginate( circle.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")