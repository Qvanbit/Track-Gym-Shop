from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.gateways.postgresql.database import get_async_session
from src.core.gateways.postgresql.reposetories.shop.category import CategoryRepository
from src.core.application.api.v1.shop.schemas.category import GetCategoryListResponseSchema
from src.core.logic.services.shop.category import CategoryService


router = APIRouter(tags=['category'])

def get_category_service(session: AsyncSession = Depends(get_async_session)) -> CategoryService:
    repository = CategoryRepository(session)
    return CategoryService(repository)


@router.get(
    '/category',
    description='Эндпоинт возвращает список категорий товаров',
    responses={
            status.HTTP_200_OK: {'model': GetCategoryListResponseSchema},
        },
)
async def get_category_list_handler(service: CategoryService = Depends(get_category_service)):
    return await service.get_category_list()