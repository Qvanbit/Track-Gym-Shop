from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import Mapped, relationship

from src.core.domain.entities.shop.product import ProductEntity
from src.core.gateways.postgresql.models.base import Base
from src.core.gateways.postgresql.models.shop.association import category_product

class ProductORM(Base):
    __tablename__ = 'product'
    
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = Column(String(150), unique=True, nullable=False, comment="Название товара")
    slug: Mapped[str] = Column(String(200), unique=True, nullable=False, comment="URL")
    description: Mapped[str] = Column(Text, nullable=False, comment="Описание товара")
    full_description: Mapped[str] = Column(Text, nullable=False, comment="Полное описание товара, включая состав и прочую информацию")
    image: Mapped[str] = Column(String(200), nullable=True, comment="Изображение товара")
    
    price: Mapped[int] = Column(Integer, default=0, nullable=False, comment="Цена товара")
    quantity: Mapped[int] = Column(Integer, default=0, nullable=False, comment="Количество товара")
    size: Mapped[int] = Column(Integer, default=0, nullable=False, comment="Размер товара в г или мл")
    
    is_visible: Mapped[bool] = Column(Boolean, default=True, comment="Отображение товара")
    
    calories: Mapped[int] = Column(Integer, default=0, nullable=False, comment="Каллорий В порции, г")
    protein: Mapped[int] = Column(Integer, default=0, nullable=False, comment="Белков В порции, г")
    carbohydrate: Mapped[int] = Column(Integer, default=0, nullable=False, comment="Углеводов В порции, г")
    fat: Mapped[int] = Column(Integer, default=0, nullable=False, comment="Жиров В порции, г")
    
    categories: Mapped[list["CategoryORM"]] = relationship("CategoryORM", secondary=category_product, back_populates="products") # type: ignore
    
    @staticmethod
    def from_entity(obj: ProductEntity) -> "ProductORM":
        return ProductORM(
            id=obj.id,
            title=obj.title,
            slug=obj.slug,
            description=obj.description,
            full_description=obj.full_description,
            image=obj.image,
            price=obj.price,
            quantity=obj.quantity,
            size=obj.size,
            calories=obj.calories,
            protein=obj.protein,
            carbohydrate=obj.carbohydrate,
            fat=obj.fat,
            # categories=[CategoryORM.from_entity(category) for category in obj.categories],  # type: ignore
        )
    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            price=self.price,
            quantity=self.quantity,
            size=self.size,
            calories=self.calories,
            protein=self.protein,
            carbohydrate=self.carbohydrate,
            fat=self.fat,
            created_at=self.created_at,
            updated_at=self.updated_at,
            # categories=[category.to_entity() for category in self.categories],  # type: ignore
        )
    
    def __repr__(self):
        return f"<Product(title={self.title}>"
