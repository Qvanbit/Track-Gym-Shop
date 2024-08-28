from sqlalchemy import Column, ForeignKey, Integer, Table

from src.core.gateways.postgresql.models.base import Base

category_product = Table(
    'category_product', Base.metadata,
    Column('category_id', Integer(), ForeignKey('category.id')),
    Column('product_id', Integer(), ForeignKey('product.id')),
)