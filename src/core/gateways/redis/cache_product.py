from typing import List
from src.core.application.api.v1.shop.schemas.product import GetProductListResponseSchema, ProductListResponseSchema
from src.core.gateways.redis.redis import redis_cache
from src.core.logic.services.shop.product import ProductEntity

CACHE_KEY = 'product_list'

async def get_cached_product_list() -> GetProductListResponseSchema:
    cached_data = await redis_cache.get(CACHE_KEY)
    if cached_data:
        return GetProductListResponseSchema.model_validate_json(cached_data)
    return None

async def set_product_list_to_cache(product_entities: List[ProductEntity]):
    product_list = [ProductListResponseSchema.from_entity(product) for product in product_entities]
    response_data = GetProductListResponseSchema(product_list=product_list)
    await redis_cache.set(CACHE_KEY, response_data.model_dump_json(), expire=300)

