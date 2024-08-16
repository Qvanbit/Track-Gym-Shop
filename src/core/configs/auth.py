from src.core.configs.base import Settings

class AuthSettings(Settings):
    JWT_TOKEN: str
    MANAGER_TOKEN: str
    VERIFICATION_TOKEN: str
        