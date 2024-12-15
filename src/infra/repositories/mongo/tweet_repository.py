from bson import ObjectId
from typing import Any
from pymongo.asynchronous.client_session import AsyncClientSession
from pymongo.asynchronous.collection import AsyncCollection
from src.domain.entities import Tweet
from src.domain.repositories import TweetRepository


class MongoTweetRepository(TweetRepository):
    def __init__(self, session: AsyncClientSession, collection: AsyncCollection) -> None:
        self.collection = collection
        self.session = session

    async def list_by(self, **kwargs) -> list[Tweet]:
        filters = {}

        if kwargs.get("user_id"):
            filters["user_id"] = ObjectId(kwargs.pop("user_id"))

        cursor = self.collection.find(
            filters,
            session=self.session,
        )

        return [
            Tweet(
                id=str(tweet_data.pop("_id")),
                user_id=str(tweet_data.pop("user_id")),
                **tweet_data,
            )
            async for tweet_data in cursor
        ]

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
        tweet_model["user_id"] = ObjectId(tweet_model["user_id"])

        await self.collection.insert_one(tweet_model, session=self.session)
