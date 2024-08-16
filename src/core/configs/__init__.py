from src.core.configs.auth import AuthSettings
from src.core.configs.fastapi import FastApiSettings
from src.core.configs.pgadmin import PgAdminSettings
from src.core.configs.postgres import PostgresSettings
from src.core.configs.telegram import TelegramSettings

class Settings(
    TelegramSettings,
    FastApiSettings,
    PostgresSettings,
    PgAdminSettings,
    AuthSettings,
):
    class Config:
        case_sensitive = True
        env_file = '.env'
        
settings = Settings()