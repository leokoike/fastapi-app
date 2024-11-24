from bson import ObjectId
from typing import Any
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClientSession
from src.domain.entities import Tweet
from src.domain.repositories import TweetRepository


class MongoTweetRepository(TweetRepository):
    def __init__(self, session: AsyncIOMotorClientSession, collection: AsyncIOMotorCollection) -> None:
        self.collection = collection
        self.session = session

    async def list_by(self, **kwargs) -> list[Tweet]:
        raise NotImplementedError()

    async def find_by(self, **kwargs) -> Tweet | None:
        filters = {}

        if kwargs.get("id"):
            filters["_id"] = ObjectId(kwargs.pop("id"))

        tweet_data: dict[str, Any] | None = await self.collection.find_one(
            filters,
            session=self.session,
        )

        if tweet_data:
            tweet_data["id"] = str(tweet_data["_id"])
            tweet_data["user_id"] = str(tweet_data["user_id"])
            return Tweet(**tweet_data)

    async def create(self, tweet: Tweet) -> None:
        tweet_model = tweet.model_dump(exclude_none=True)

        await self.collection.insert_one(tweet_model, session=self.session)
