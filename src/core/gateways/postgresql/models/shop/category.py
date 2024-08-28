from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped, relationship


from src.core.domain.entities.shop.category import CategoryEntity
from src.core.gateways.postgresql.models.base import Base
from src.core.gateways.postgresql.models.shop.association import category_product

from src.core.gateways.postgresql.models.shop.product import ProductORM

class CategoryORM(Base):
    __tablename__ = 'category'
    
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(150), unique=True, nullable=False, comment="Название")
    slug: Mapped[str] = Column(String(200), unique=True, nullable=True, comment="URL")
    is_visible: Mapped[bool] = Column(Boolean, default=True, comment="Отображение категории")
    
    products: Mapped[list['ProductORM']]= relationship('ProductORM', secondary=category_product, back_populates='categories') # type: ignore
    
    def to_entity(self) -> CategoryEntity:
        return CategoryEntity(
            id=self.id,
            name=self.name,
            slug=self.slug,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    def __repr__(self):
        return f"<Category(name={self.name})>"
