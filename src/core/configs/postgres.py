from src.core.configs.base import Settings

class PostgresSettings(Settings):
    POSTGRES_PORT: str
    POSTGRES_HOST: str
    POSTGRES_HOST_DOCKER: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str