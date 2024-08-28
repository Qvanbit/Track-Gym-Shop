from abc import ABC, abstractmethod
from typing import Iterable, List
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.gateways.postgresql.models.shop.category import CategoryORM
from src.core.domain.entities.shop.category import CategoryEntity


class BaseCategoryRepository(ABC):
    @abstractmethod
    async def get_category_list(self) -> Iterable[CategoryEntity]: ...


@dataclass
class CategoryRepository(BaseCategoryRepository):
    session: AsyncSession

    async def get_category_list(self) -> List[CategoryEntity]:
        query = select(CategoryORM)
        result = await self.session.execute(query)
        category_list = result.scalars().all()
        return [
            CategoryEntity(id=category.id, name=category.name, slug=category.slug)
            for category in category_list
        ]
