from typing import Any
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClientSession
from src.domain.entities.user import User
from src.domain.repositories import UserRepository


class MongoUserRepository(UserRepository):
    def __init__(self, session: AsyncIOMotorClientSession, collection: AsyncIOMotorCollection) -> None:
        self.collection = collection
        self.session = session

    async def find_by(self, **kwargs) -> User | None:
        user_data: dict[str, Any] | None = await self.collection.find_one(kwargs, session=self.session)

        if user_data:
            return User(**user_data)

    async def create(self, user: User) -> None:
        user_model = user.model_dump(exclude=["_id"])

        await self.collection.insert_one(user_model, session=self.session)
