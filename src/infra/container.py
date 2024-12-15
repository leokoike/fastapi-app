from fastapi import Request, Depends
from pymongo.asynchronous.client_session import AsyncClientSession
from pymongo.asynchronous.collection import AsyncCollection

from src.domain.repositories import UserRepository, TweetRepository
from src.domain.use_cases import (
    CreateUserUseCase,
    FindUserUseCase,
    CreateTweetUseCase,
    FindTweetUseCase,
    CreateTokenUseCase,
    DecodeTokenUseCase,
    AuthenticateUseCase,
)
from src.domain.utils.security import HashingData
from src.infra.config import settings
from src.infra.databases.mongo.connection import MongoConnection
from src.infra.repositories import MongoUserRepository, MongoTweetRepository


__all__ = [
    "get_authenticate_use_case",
    "get_db_conn",
    "get_db_session",
    "get_create_token_use_case",
    "get_create_tweet_use_case",
    "get_create_user_use_case",
    "get_decode_token_use_case",
    "get_find_tweet_use_case",
    "get_find_user_use_case",
    "get_hashing_data",
]


async def get_hashing_data() -> HashingData:
    return HashingData()


async def get_db_conn(request: Request) -> MongoConnection:
    return request.state.conn


async def get_db_session(request: Request) -> AsyncClientSession:
    return request.state.session


async def get_user_repository(
    session: AsyncClientSession = Depends(get_db_session),
) -> UserRepository:
    collection: AsyncCollection = session.client[settings.database_name][settings.users_collection]
    return MongoUserRepository(session=session, collection=collection)


async def get_tweet_repository(
    session: AsyncClientSession = Depends(get_db_session),
) -> TweetRepository:
    collection: AsyncCollection = session.client[settings.database_name][settings.tweets_collection]
    return MongoTweetRepository(session=session, collection=collection)


async def get_create_user_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
    hashing_data: HashingData = Depends(get_hashing_data),
) -> CreateUserUseCase:
    return CreateUserUseCase(
        user_repository=user_repository,
        hashing_data=hashing_data,
    )


async def get_find_user_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> FindUserUseCase:
    return FindUserUseCase(user_repository=user_repository)


async def get_create_tweet_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
    tweet_repository: TweetRepository = Depends(get_tweet_repository),
) -> CreateTweetUseCase:
    return CreateTweetUseCase(
        user_repository=user_repository,
        tweet_repository=tweet_repository,
    )


async def get_find_tweet_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
    tweet_repository: TweetRepository = Depends(get_tweet_repository),
) -> FindTweetUseCase:
    return FindTweetUseCase(
        user_repository=user_repository,
        tweet_repository=tweet_repository,
    )


async def get_authenticate_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
    hashing_data: HashingData = Depends(get_hashing_data),
) -> AuthenticateUseCase:
    return AuthenticateUseCase(
        user_repository=user_repository,
        hashing_data=hashing_data,
    )


async def get_create_token_use_case() -> CreateTokenUseCase:
    return CreateTokenUseCase()


async def get_decode_token_use_case() -> DecodeTokenUseCase:
    return DecodeTokenUseCase()
