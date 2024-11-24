from datetime import datetime, UTC
from src.domain.dtos import CreateTweet
from src.domain.entities import User, Tweet
from src.domain.repositories import TweetRepository, UserRepository
from src.domain.utils.errors import BusinessException


class CreateTweetUseCase:
    def __init__(self, tweet_repository: TweetRepository, user_repository: UserRepository) -> None:
        self.tweet_repository = tweet_repository
        self.user_repository = user_repository

    async def execute(self, create_tweet: CreateTweet) -> None:
        user: User | None = await self.user_repository.find_by(id=create_tweet.user_id)

        if not user:
            raise BusinessException(message="User not found")

        now = datetime.now(UTC)

        new_tweet = Tweet(
            created_at=now,
            updated_at=now,
            content=create_tweet.content,
            user_id=create_tweet.user_id,
        )

        await self.tweet_repository.create(tweet=new_tweet)
