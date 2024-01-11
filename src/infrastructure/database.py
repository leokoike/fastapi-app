from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_scoped_session,
    async_sessionmaker,
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


AsyncScopedSession = async_scoped_session(
    sessionmaker,
    scopefunc=current_task,
)

Base: registry = declarative_base()
