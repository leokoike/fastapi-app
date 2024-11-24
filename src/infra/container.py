from fastapi import Request, Depends
from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection

from src.domain.repositories import UserRepository
from src.domain.use_cases import CreateUserUseCase
from src.infra.config import settings
from src.infra.databases.mongo.connection import MongoConnection
from src.infra.repositories import MongoUserRepository


async def get_db_conn(request: Request) -> MongoConnection:
    return request.state.conn


async def get_db_session(request: Request) -> AsyncIOMotorClientSession:
    return request.state.session


async def get_user_repository(
    session: AsyncIOMotorClientSession = Depends(get_db_session),
) -> UserRepository:
    collection: AsyncIOMotorCollection = session.client[settings.database_name][settings.users_collection]
    return MongoUserRepository(session=session, collection=collection)


async def get_create_user_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository=user_repository)
