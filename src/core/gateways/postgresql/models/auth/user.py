from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.gateways.postgresql.models.base import Base

class RoleORM(Base):
    __tablename__ = 'role'
    
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, nullable=False)
    permissions: Mapped[JSON] = Column(JSON)
    
    
class UserORM(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    role_id: Mapped[int] = Column(Integer, ForeignKey(RoleORM.id))

