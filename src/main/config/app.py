from fastapi import FastAPI

from .middlewares import create_middlewares
from .routes import create_routes


def create_app() -> FastAPI:
    app = FastAPI(
        title='Recomendação de Óculos',
        version='3.0.0',
        # servers=[{
        #     'url': '/api',
        #     'description': 'Servidor Principal'
        # }]
    )
    create_middlewares(app)
    create_routes(app)

    return app
