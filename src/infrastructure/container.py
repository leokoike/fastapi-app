from fastapi import Depends, Request
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.security.token import TokenResolver
from src.infrastructure.config import settings
from src.infrastructure.security.fernet.fernet_data_crypto import FernetDataCrypto
from src.infrastructure.repositories.pg import PgUserRepository
from src.domain.security.data_crypto import DataCrypto
from src.domain.usecases.user import ListUsersUseCase, CreateUserUseCase
from src.domain.repositories import UserRepository
from src.infrastructure.security.jwt.token import JWTTokenResolver


def _get_session(request: Request) -> AsyncSession:
    return request.state.session


def _user_repository(session: Annotated[AsyncSession, Depends(_get_session)]) -> PgUserRepository:
    return PgUserRepository(session=session)


def _data_crypto() -> DataCrypto:
    return FernetDataCrypto(key=settings.CRYPTO_KEY)


def _token_resolver() -> TokenResolver:
    return JWTTokenResolver()


def get_list_users_usecase(
    user_repository: Annotated[UserRepository, Depends(_user_repository)],
) -> ListUsersUseCase:
    return ListUsersUseCase(user_repository)


def get_create_user_usecase(
    user_repository: Annotated[UserRepository, Depends(_user_repository)],
    data_crypto: Annotated[DataCrypto, Depends(_data_crypto)],
) -> CreateUserUseCase:
    return CreateUserUseCase(
        user_repository,
        data_crypto,
    )
