from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database import get_session
from src.infrastructure.pg_repositories import PgProjectRespository


def project_repository(session: Annotated[AsyncSession, Depends(get_session)]) -> PgProjectRespository:
    return PgProjectRespository(session=session)
