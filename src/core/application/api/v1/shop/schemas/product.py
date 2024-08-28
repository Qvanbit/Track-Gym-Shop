from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.core.domain.entities.shop.product import ProductEntity


class ProductListResponseSchema(BaseModel):
    id: int  # noqa
    title: str
    description: str
    price: int
    quantity: int
    size: int
    calories: int
    protein: int
    carbohydrate: int
    fat: int
    created_at: datetime
    updated_at: datetime | None = None
    
    @staticmethod
    def from_entity(entity: ProductEntity) -> 'ProductListResponseSchema':
        return ProductListResponseSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            price=entity.price,
            quantity=entity.quantity,
            size=entity.size,
            calories=entity.calories,
            protein=entity.protein,
            carbohydrate=entity.carbohydrate,
            fat=entity.fat,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

class GetProductListResponseSchema(BaseModel):
    product_list: List[ProductListResponseSchema]