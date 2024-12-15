from bson import ObjectId
from typing import Any
from pymongo.asynchronous.client_session import AsyncClientSession
from pymongo.asynchronous.collection import AsyncCollection
from src.domain.entities.user import User
from src.domain.repositories import UserRepository


class MongoUserRepository(UserRepository):
    def __init__(self, session: AsyncClientSession, collection: AsyncCollection) -> None:
        self.collection = collection
        self.session = session

    async def find_by(self, **kwargs) -> User | None:
        filters = {}

        if kwargs.get("id"):
            filters["_id"] = ObjectId(kwargs.pop("id"))

        filters |= kwargs

        user_data: dict[str, Any] | None = await self.collection.find_one(
            filters,
            session=self.session,
        )

        if user_data:
            user_data["id"] = str(user_data["_id"])
            return User(**user_data)

    async def create(self, user: User) -> None:
        user_model = user.model_dump(exclude_none=True)

        await self.collection.insert_one(user_model, session=self.session)
