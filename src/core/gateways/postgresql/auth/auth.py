from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from src.core.configs import settings

cookie_transport = CookieTransport(cookie_name='health shop',cookie_max_age=3600)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.JWT_TOKEN, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)