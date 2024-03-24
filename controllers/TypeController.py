from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Type import Type
from schemas import TypeBase, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Type Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ TypeBase ]:
	return paginate_query( db, select(Type).order_by( Type.TypeId ) )

@router.get('/{type_Id}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, type_Id: int = Path( gt=0 ) ) -> TypeBase:
	type_ = db.query(Type).filter( Type.TypeId == type_Id ).first()

	if type_ is not None:
		return type_
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{type_Id}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, type_Id: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	type_ = db.query(Type).filter( Type.TypeId == type_Id ).first()

	if type_ is not None:
		return paginate( type_.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")