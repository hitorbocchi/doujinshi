from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated, Union
from enum import Enum

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Content import Content
from schemas import ContentBase, ContentDetail, AuthorBase, BookCatalog, CharacterBase, CircleBase, ConventionBase, TypeBase

class ModelName(str, Enum):
	Author     = 'authors'
	Book       = 'books'
	Character  = 'characters'
	Circle     = 'circles'
	Convention = 'conventions'
	Parody     = 'parodies'

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Content Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ ContentBase ]:
	return paginate_query( db, select(Content).order_by( Content.ContentId ) )

@router.get('/{contentId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, contentId: int = Path( gt=0 ) ) -> ContentDetail:
	content = db.query(Content).filter( Content.ContentId == contentId ).first()

	if content is not None:
		return content
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{contentId}/{model}', status_code=status.HTTP_200_OK)
def showModel( db: db_dependency, contentId: int = Path( gt=0 ), model: ModelName = '' ) -> Page[ Union[ AuthorBase, BookCatalog, CharacterBase, CircleBase, ConventionBase, TypeBase ] ]:
	content = db.query(Content).filter( Content.ContentId == contentId ).first()

	if content is not None:
		return paginate( getattr( content, model ) )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")