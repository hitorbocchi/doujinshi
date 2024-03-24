from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Imprint import Imprint
from schemas import ImprintBase, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Imprint Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ ImprintBase ]:
	return paginate_query( db, select(Imprint).order_by( Imprint.ImprintId ) )

@router.get('/{imprintId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, imprintId: int = Path( gt=0 ) ) -> ImprintBase:
	imprint = db.query(Imprint).filter( Imprint.ImprintId == imprintId ).first()

	if imprint is not None:
		return imprint
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{imprintId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, imprintId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	imprint = db.query(Imprint).filter( Imprint.ImprintId == imprintId ).first()

	if imprint is not None:
		return paginate( imprint.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")