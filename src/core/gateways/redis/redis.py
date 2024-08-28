import aioredis
from typing import Optional

from src.core.configs import settings

class RedisCache:
    def __init__(self, url: str):
        self.url = url
        self.redis = None

    async def initialize(self):
        self.redis = await aioredis.from_url(self.url, decode_responses=True)

    async def close(self):
        if self.redis:
            await self.redis.close()

    async def set(self, key: str, value: str, expire: Optional[int] = None):
        await self.redis.set(key, value, ex=expire)

    async def get(self, key: str) -> Optional[str]:
        return await self.redis.get(key)

    async def delete(self, key: str):
        await self.redis.delete(key)

# Создание глобального экземпляра RedisCache
redis_cache = RedisCache(url=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
