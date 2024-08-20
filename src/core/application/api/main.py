from fastapi import FastAPI

from src.core.application.api.router import router as router_main
from src.core.application.api.v1.operations.router import router as router_operations
from src.core.application.api.v1.auth.router import router as router_auth


def create_app() -> FastAPI:
    app = FastAPI(
        title='Track Gym Service for your sport',
        docs_url='/api/docs',
        description='Сервис TRack Gym для вашего спорта.',
        debug=True,
    )
    
    app.include_router(router_main)
    app.include_router(router_auth)
    app.include_router(router_operations)

    return app