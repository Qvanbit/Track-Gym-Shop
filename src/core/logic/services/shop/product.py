from abc import ABC, abstractmethod
from dataclasses import dataclass
import time
from typing import List

from src.core.domain.entities.shop.product import ProductEntity
from src.core.gateways.postgresql.reposetories.shop.product import ProductRepository


class BaseProductService(ABC):
    @abstractmethod
    async def get_product_list(self): ...

@dataclass
class ProductService:
    product_repository: ProductRepository

    async def get_product_list(self) -> List[ProductEntity]:
        time.sleep(5)
        return await self.product_repository.get_product_list()

