from src.core.configs.base import Settings

class RedisSettings(Settings):
    REDIS_PORT: str
    REDIS_HOST: str