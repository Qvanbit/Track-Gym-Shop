from sqlalchemy import Table, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped

from src.core.gateways.postgresql.models.base import Base

class Operation(Base):
    __tablename__ = 'operation'
    
    id: Mapped[int] = Column(Integer, primary_key=True)
    quantity: Mapped[str] = Column(String)
    figi: Mapped[str] = Column(String)
    
    
    