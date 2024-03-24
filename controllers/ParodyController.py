from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Parody import Parody
from schemas import ParodyBase, ParodyDetail, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Parody Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ ParodyBase ]:
	return paginate_query( db, select(Parody).order_by( Parody.ParodyId ) )

@router.get('/{parodyId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, parodyId: int = Path( gt=0 ) ) -> ParodyDetail:
	parody = db.query(Parody).filter( Parody.ParodyId == parodyId ).first()

	if parody is not None:
		return parody
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{parodyId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, parodyId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	parody = db.query(Parody).filter( Parody.ParodyId == parodyId ).first()

	if parody is not None:
		return paginate( parody.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")