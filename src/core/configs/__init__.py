from src.core.configs.auth import AuthSettings
from src.core.configs.fastapi import FastApiSettings
from src.core.configs.pgadmin import PgAdminSettings
from src.core.configs.postgres import PostgresSettings
from src.core.configs.telegram import TelegramSettings
from src.core.configs.redis import RedisSettings

class Settings(
    TelegramSettings,
    FastApiSettings,
    PostgresSettings,
    PgAdminSettings,
    AuthSettings,
    RedisSettings,
):
    class Config:
        case_sensitive = True
        env_file = '.env'
        
settings = Settings()