from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.core.domain.entities.shop.category import CategoryEntity
from src.core.gateways.postgresql.reposetories.shop.category import CategoryRepository

class BaseCategoryService(ABC):
    @abstractmethod
    async def get_category_list(self) -> List[CategoryEntity]:
        ...

@dataclass
class CategoryService(BaseCategoryService):
    category_repository: CategoryRepository
        
    async def get_category_list(self) -> List[CategoryEntity]:
        return await self.category_repository.get_category_list()

