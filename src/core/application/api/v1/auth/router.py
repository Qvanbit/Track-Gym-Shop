from fastapi import APIRouter, Depends

from src.core.logic.auth.auth import auth_backend
from src.core.application.api.v1.auth.schemas import UserCreate, UserRead
from src.core.gateways.postgresql.models.auth.user import User

from src.core.logic.auth.auth import fastapi_users, current_user



router = APIRouter(tags=['auth'])

router.include_router(fastapi_users.get_auth_router(auth_backend),
                      prefix='/auth/jwt')

router.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
                      prefix='/auth')

@router.get("/protected-route")
async def protected_route(user: User = Depends(current_user)):
        return f"Hi, {user.email}"
    
@router.get("/unprotected-route")
async def unprotected_route():
        return f"Hi, go register"
    

