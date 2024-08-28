from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProductEntity:
    id: int  # noqa
    title: str
    description: str
    quantity: int
    price: int
    size: int
    calories: int
    fat: int
    protein: int
    carbohydrate: int
    created_at: datetime
    updated_at: datetime
