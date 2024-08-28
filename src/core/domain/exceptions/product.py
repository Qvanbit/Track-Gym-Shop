from dataclasses import dataclass

from src.core.domain.exceptions.base import ServiceException

@dataclass(eq=False)
class ProductNotFoundException(ServiceException):
    product_id: int
    
    @property
    def message(self):
        return f"Product with ID {self.product_id} not found"