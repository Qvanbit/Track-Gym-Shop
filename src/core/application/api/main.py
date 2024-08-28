from fastapi import FastAPI

from src.core.gateways.redis.redis import redis_cache
 
from src.core.application.api.router import router as router_main
from src.core.application.api.v1.auth.router import router as router_auth
from src.core.application.api.v1.shop.router.category import router as router_category
from src.core.application.api.v1.shop.router.product import router as router_product


def create_app() -> FastAPI:
    app = FastAPI(
        title='Track Gym Service for your sport',
        docs_url='/api/docs',
        description='Сервис Track Gym для вашего спорта.',
        debug=True,
    )
    
    @app.on_event("startup")
    async def startup():
        await redis_cache.initialize()

    @app.on_event("shutdown")
    async def shutdown():
        await redis_cache.close()

    app.add_event_handler("shutdown", redis_cache.close)
    
    app.include_router(router_main)
    app.include_router(router_auth)
    app.include_router(router_category)
    app.include_router(router_product)

    return app
