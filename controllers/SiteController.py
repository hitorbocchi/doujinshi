from fastapi import APIRouter, status, Depends, HTTPException, Query
from typing import Annotated, Union
from enum import Enum

from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_query

from dependencies import get_db

from models import Author, Book, Character, Circle, Collection, Convention, Imprint, Parody, Publisher
from schemas import AuthorBase, BookCatalog, CharacterBase, CircleBase, ConventionBase, ImprintBase, ParodyBase, PublisherBase, TypeBase

class ModelName(str, Enum):
	Author     = 'author'
	Book       = 'book'
	Character  = 'character'
	Circle     = 'circle'
	Collection = 'collection'
	Convention = 'convention'
	Imprint    = 'imprint'
	Parody     = 'parody'
	Publisher  = 'publisher'

db_dependency = Annotated[ Session, Depends( get_db ) ]

router = APIRouter()

@router.get('/search', status_code=status.HTTP_200_OK)
def search( 
	db: db_dependency, 
	data:  ModelName, 
	q: Annotated[str, Query(min_length = 1)] 
) -> Page[ Union[ AuthorBase, BookCatalog, CharacterBase, CircleBase, ConventionBase, ImprintBase, ParodyBase, PublisherBase, TypeBase ] ]:
	
	search = "%{}%".format(q)

	if data == 'author':
		query = select( Author.Author ).filter( or_( Author.Author.Name_EN.like( search ), Author.Author.Name_JP.like( search ), Author.Author.Name_R.like( search ) ) )
	elif data == 'book':
		query = select( Book.Book ).filter( or_( Book.Book.Name_EN.like( search ), Book.Book.Name_JP.like( search ), Book.Book.Name_R.like( search ) ) )
	elif data == 'character':
		query = select( Character.Character ).filter( or_( Character.Character.Name_EN.like( search ), Character.Character.Name_JP.like( search ), Character.Character.Name_R.like( search ) ) )
	elif data == 'circle':
		query = select( Circle.Circle ).filter( or_( Circle.Circle.Name_EN.like( search ), Circle.Circle.Name_JP.like( search ), Circle.Circle.Name_R.like( search ) ) )
	elif data == 'collection':
		query = select( Collection.Collection ).filter( or_( Collection.Collection.Name_EN.like( search ), Collection.Collection.Name_JP.like( search ), Collection.Collection.Name_R.like( search ) ) )
	elif data == 'convention':
		query = select( Convention.Convention ).filter( or_( Convention.Convention.Name_EN.like( search ), Convention.Convention.Name_JP.like( search ), Convention.Convention.Name_R.like( search ) ) )
	elif data == 'imprint':
		query = select( Imprint.Imprint ).filter( or_( Imprint.Imprint.Name_EN.like( search ), Imprint.Imprint.Name_JP.like( search ), Imprint.Imprint.Name_R.like( search ) ) )
	elif data == 'parody':
		query = select( Parody.Parody ).filter( or_( Parody.Parody.Name_EN.like( search ), Parody.Parody.Name_JP.like( search ), Parody.Parody.Name_R.like( search ) ) )
	elif data == 'publisher':
		query = select( Publisher.Publisher ).filter( or_( Publisher.Publisher.Name_EN.like( search ), Publisher.Publisher.Name_JP.like( search ), Publisher.Publisher.Name_R.like( search ) ) )
	else:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

	return paginate_query( db, query )