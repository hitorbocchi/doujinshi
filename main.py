from fastapi import FastAPI
from fastapi_pagination import add_pagination

from controllers import SiteController, AuthorController, BookController, CharacterController, CircleController, CollectionController, ContentController, ConventionController, GenreController, ImprintController, ParodyController, PublisherController, TypeController

app = FastAPI()

add_pagination(app)

app.include_router( SiteController.router )

app.include_router( AuthorController.router,     prefix = '/author',     tags=['Author'] )
app.include_router( BookController.router,       prefix = '/book',       tags=['Book'] )
app.include_router( CharacterController.router,  prefix = '/character',  tags=['Character'] )
app.include_router( CircleController.router,     prefix = '/circle',     tags=['Circle'] )
app.include_router( CollectionController.router, prefix = '/collection', tags=['Collection'] )
app.include_router( ContentController.router,    prefix = '/content',    tags=['Content'] )
app.include_router( ConventionController.router, prefix = '/convention', tags=['Convention'] )
app.include_router( GenreController.router,      prefix = '/genre',      tags=['Genre'] )
app.include_router( ImprintController.router,    prefix = '/imprint',    tags=['Imprint'] )
app.include_router( ParodyController.router,     prefix = '/parody',     tags=['Parody'] )
app.include_router( PublisherController.router,  prefix = '/publisher',  tags=['Publisher'] )
app.include_router( TypeController.router,       prefix = '/type',       tags=['Type'] )