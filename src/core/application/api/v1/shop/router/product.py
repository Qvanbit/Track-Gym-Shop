from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession


from src.core.gateways.postgresql.database import get_async_session
from src.core.gateways.postgresql.reposetories.shop.product import ProductRepository
from src.core.gateways.redis.cache_product import get_cached_product_list, set_product_list_to_cache
from src.core.logic.services.shop.product import ProductService
from src.core.application.api.v1.shop.schemas.product import (
    GetProductListResponseSchema,
    ProductListResponseSchema
)
from src.core.gateways.redis.redis import redis_cache

router = APIRouter(tags=["product"])


def get_product_service(
    session: AsyncSession = Depends(get_async_session),
) -> ProductService:
    repository = ProductRepository(session)
    return ProductService(repository)


@router.get(
    "/products",
    description="Эндпоинт, который возвращает список всех продуктов",
    responses={
        status.HTTP_200_OK: {"model": GetProductListResponseSchema},
    },
)
async def get_product_list_handler(
    service: ProductService = Depends(get_product_service),
):
    response_data = await get_cached_product_list()
    if response_data:
        return response_data
    product_entities = await service.get_product_list()
    await set_product_list_to_cache(product_entities)
    return await get_cached_product_list()

