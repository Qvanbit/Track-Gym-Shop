from fastapi import FastAPI

from fastapi_users import FastAPIUsers

from src.core.application.api.v1.auth.schemas import UserCreate, UserRead
from src.core.gateways.postgresql.auth import auth_backend
from src.core.gateways.postgresql.auth.manager import get_user_manager
from src.core.gateways.postgresql.models.auth.user import User

def create_app() -> FastAPI:
    app = FastAPI(
        title='Application was successfully created',
        docs_url='/api/docs',
        description='It is a simle application, that tell you, that all good',
        debug=True,
    )
    
    fastapi_users = FastAPIUsers[User, int](
        get_user_manager,
        [auth_backend]
    )
    
    @app.get("/")
    async def read_root():
        return {"message": "All good"}
    
    app.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix='/auth/jwt',
        tags=["auth"],
    )
    
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix='/auth',
        tags=["auth"],
    )
    return app