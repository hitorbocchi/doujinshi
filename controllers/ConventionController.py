from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Convention import Convention
from schemas import ConventionBase, ConventionDetail, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Convention Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ ConventionBase ]:
	return paginate_query( db, select(Convention).order_by( Convention.ConventionId ) )

@router.get('/{conventionId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, conventionId: int = Path( gt=0 ) ) -> ConventionDetail:
	convention = db.query(Convention).filter( Convention.ConventionId == conventionId ).first()

	if convention is not None:
		return convention
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{conventionId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, conventionId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	convention = db.query(Convention).filter( Convention.ConventionId == conventionId ).first()

	if convention is not None:
		return paginate( convention.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")