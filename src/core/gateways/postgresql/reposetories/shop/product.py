from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.domain.entities.shop.product import ProductEntity
from src.core.gateways.postgresql.models.shop.product import ProductORM


class BaseProductRepository(ABC):
    @abstractmethod
    async def get_product_list(self) -> Iterable[ProductEntity]: ...


@dataclass
class ProductRepository(BaseProductRepository):
    session: AsyncSession

    async def get_product_list(self) -> List[ProductEntity]:
        query = select(ProductORM)
        result = await self.session.execute(query)
        product_list = result.scalars().all()
        return [
            product.to_entity() for product in product_list]
