from fastapi import Depends, Request
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.pg_repositories import PgUserRepository
from src.domain.usecases.user import ListUsersUseCase, CreateUserUseCase
from src.domain.repositories import UserRepository


def _get_session(request: Request):
    return request.state.session


def _user_repository(session: Annotated[AsyncSession, Depends(_get_session)]) -> PgUserRepository:
    return PgUserRepository(session=session)


def get_list_users_usecase(user_repository: Annotated[UserRepository, Depends(_user_repository)]) -> ListUsersUseCase:
    return ListUsersUseCase(user_repository)


def get_create_user_usecase(user_repository: Annotated[UserRepository, Depends(_user_repository)]) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository)
