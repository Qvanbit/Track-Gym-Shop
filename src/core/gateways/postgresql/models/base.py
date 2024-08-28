from typing import Any
from sqlalchemy import Column, DateTime, Integer, MetaData, func
from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy.ext.declarative import declared_attr


metadata = MetaData()

BaseORM = declarative_base(metadata=metadata)

class Base(BaseORM):
    id: Mapped[int] = Column(Integer, primary_key=True)
    __abstract__ = True
    __name__: str
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    created_at: Mapped[DateTime] = Column(DateTime, default=func.now(), nullable=False, comment="Дата создания записи")
    updated_at: Mapped[DateTime] = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False, comment="Дата обновления записи")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
