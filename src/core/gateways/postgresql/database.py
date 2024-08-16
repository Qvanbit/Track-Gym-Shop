import logging
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.exc import SQLAlchemyError

from src.core.configs import settings
from src.core.gateways.postgresql.models.base import Base
from src.core.gateways.postgresql.models.auth.user import User

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Формируем URL для подключения к базе данных
DATABASE_URL = (
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST_DOCKER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)

# Создаем движок SQLAlchemy с логированием запросов
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Функция для получения асинхронной сессии
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    try:
        logger.info("Creating a new database session")
        async with async_session_maker() as session:
            yield session
    except SQLAlchemyError as e:
        logger.error(f"Database session creation failed: {e}")
        raise
    finally:
        logger.info("Database session closed")

# Функция для получения базы данных пользователей
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    logger.info("Getting user database")
    yield SQLAlchemyUserDatabase(session, User)
