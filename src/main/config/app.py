from fastapi import FastAPI

from .routes import create_routes


def create_app() -> FastAPI:
    app = FastAPI(
        title='Recomendação de Óculos',
        version='1.4.0',
        # servers=[{
        #     'url': '/api',
        #     'description': 'Servidor Principal'
        # }]
    )
    create_routes(app)

    return app
