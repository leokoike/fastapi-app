from typing import AsyncIterator
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncSessionTransaction,
)
from sqlalchemy.orm import declarative_base, registry
from sqlalchemy.pool import NullPool

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


Base: registry = declarative_base()


# def get_session() -> AsyncSession:
#     from asyncio import current_task

#     AsyncScopedSession = async_scoped_session(
#         sessionmaker,
#         scopefunc=current_task,
#     )
#     async_session: AsyncSession = AsyncScopedSession()
#     return async_session


@asynccontextmanager
async def transaction_control(session: AsyncSession) -> AsyncIterator[AsyncSessionTransaction]:
    if session.in_transaction():
        async with session.get_transaction() as transaction:  # type: ignore
            yield transaction
    else:
        async with session.begin() as transaction:
            yield transaction
