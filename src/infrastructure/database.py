from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    async_scoped_session,
)
from sqlalchemy.orm import declarative_base, registry
from sqlalchemy.pool import NullPool
from asyncio import current_task

from src.infrastructure.config import settings

engine = create_async_engine(
    f"{settings.DATABASE_URI}/{settings.DATABASE_NAME}",
    poolclass=NullPool,
    echo=True,
    future=True,
)

sessionmaker = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)
AsyncScopedSession = async_scoped_session(
    sessionmaker,
    scopefunc=current_task,
)

Base: registry = declarative_base()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session: AsyncSession = AsyncScopedSession()
    async with async_session.begin():
        yield async_session
