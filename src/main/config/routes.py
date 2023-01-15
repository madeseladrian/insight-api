from fastapi import FastAPI

from ..routes import (
    glasses_routes,
    image_routes,
    login_routes
)


def create_routes(app: FastAPI) -> None:
    app.include_router(login_routes.router)
    app.include_router(glasses_routes.router)
    app.include_router(image_routes.router)
