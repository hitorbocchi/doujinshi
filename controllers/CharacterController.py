from fastapi import APIRouter, status, Depends, HTTPException, Path
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models.Character import Character
from schemas import CharacterBase, CharacterDetail, BookCatalog

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

'''
''
'' Character Routes
''
'''

@router.get('/', status_code=status.HTTP_200_OK)
def index( db: db_dependency ) -> Page[ CharacterBase ]:
	return paginate_query( db, select(Character).order_by( Character.CharacterId ) )

@router.get('/{characterId}', status_code=status.HTTP_200_OK)
def show( db: db_dependency, characterId: int = Path( gt=0 ) ) -> CharacterDetail:
	character = db.query(Character).filter( Character.CharacterId == characterId ).first()

	if character is not None:
		return character
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@router.get('/{characterId}/books', status_code=status.HTTP_200_OK)
def showBooks( db: db_dependency, characterId: int = Path( gt=0 ) ) -> Page[ BookCatalog ]:
	character = db.query(Character).filter( Character.CharacterId == characterId ).first()

	if character is not None:
		return paginate( character.books )
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")