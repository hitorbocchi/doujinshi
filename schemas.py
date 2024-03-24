from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class CommonBase(BaseModel):
	Name_EN: str
	Name_JP: str
	Name_R: str
	Objects: int
	Version: int

class AuthorBase(CommonBase):
	AuthorId: int
	
class BookBase(BaseModel):
	BookId: int
	Name_EN: str
	Name_JP: str
	Name_R: str
	Released: date
	Pages: int
	Age: int

class CharacterBase(CommonBase):
	CharacterId: int
	
class CircleBase(CommonBase):
	CircleId: int

class CollectionBase(CommonBase):
	CollectionId: int

class ContentBase(CommonBase):
	ContentId: int

class ConventionBase(CommonBase):
	ConventionId: int

class GenreBase(CommonBase):
	GenreId: int

class ImprintBase(CommonBase):
	ImprintId: int

class ParodyBase(CommonBase):
	ParodyId: int

class PublisherBase(CommonBase):
	PublisherId: int

class TypeBase(CommonBase):
	TypeId: int
	
class BookCatalog(BookBase):
	parodies: List['ParodyBase'] = []
	types: List['TypeBase'] = []

class BookDetail(BookCatalog):
	ISBN: int
	Anthology: int
	Language: int
	Copyshi: int
	Magazine: int
	Info: str
	authors: List['AuthorBase'] = []
	characters: List['CharacterBase'] = []
	circles: List['CircleBase'] = []
	collection: Optional['CollectionBase'] = []
	contents: List['ContentBase'] = []
	conventions: List['ConventionBase'] = []
	genres: List['GenreBase'] = []
	imprints: List['ImprintBase'] = []
	publisher: Optional['PublisherBase'] = []

class AuthorDetail(AuthorBase):
	Parent: int
	TypeId: int
	circles: List['CircleBase'] = []
	contents: List['ContentBase'] = []
	genres: List['GenreBase'] = []

class CharacterDetail(CharacterBase):
	Sex: int
	Age: int
	contents: List['ContentBase'] = []
	conventions: List['ConventionBase'] = []
	genres: List['GenreBase'] = []
	parodies: List['ParodyBase'] = []

class CircleDetail(CircleBase):
	TypeId: int
	authors: List['AuthorBase'] = []
	contents: List['ContentBase'] = []
	genres: List['GenreBase'] = []

class ContentDetail(ContentBase):
	authors: List['AuthorBase'] = []
	characters: List['CharacterBase'] = []
	circles: List['CircleBase'] = []
	conventions: List['ConventionBase'] = []
	parodies: List['ParodyBase'] = []

class ConventionDetail(ConventionBase):
	Date_Start: date
	Date_End: date
	characters: List['CharacterBase'] = []
	contents: List['ContentBase'] = []
	parodies: List['ParodyBase'] = []

class GenreDetail(GenreBase):
	authors: List['AuthorBase'] = []
	characters: List['CharacterBase'] = []
	circles: List['CircleBase'] = []
	parodies: List['ParodyBase'] = []

class ParodyDetail(ParodyBase):
	characters: List['CharacterBase'] = []
	contents: List['ContentBase'] = []
	conventions: List['ConventionBase'] = []
	genres: List['GenreBase'] = []
