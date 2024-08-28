from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from src.core.configs import settings
from src.core.gateways.postgresql.auth.manager import get_user_manager

from src.core.gateways.postgresql.models.auth.user import UserORM

cookie_transport = CookieTransport(cookie_name='healthShop',cookie_max_age=3600)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.JWT_TOKEN, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[UserORM, int](
    get_user_manager,
    [auth_backend]
    )

current_user = fastapi_users.current_user()