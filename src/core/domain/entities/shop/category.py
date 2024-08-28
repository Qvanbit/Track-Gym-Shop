from dataclasses import dataclass, field
from typing import List

# from src.core.domain.entities.shop.product import ProductEntity

@dataclass
class CategoryEntity:
    id: int
    name: str
    slug: str
    # products: List['Product'] = field(default_factory=list)