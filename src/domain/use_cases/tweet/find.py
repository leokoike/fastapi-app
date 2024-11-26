from src.domain.dtos import FindTweet
from src.domain.entities import Tweet, User
from src.domain.repositories import TweetRepository, UserRepository
from src.domain.utils.errors import BusinessException


class FindTweetUseCase:
    def __init__(self, user_repository: UserRepository, tweet_repository: TweetRepository) -> None:
        self.user_repository = user_repository
        self.tweet_repository = tweet_repository

    async def execute(self, find_tweet: FindTweet) -> Tweet:
        user: User | None = await self.user_repository.find_by(
            id=find_tweet.user_id,
        )
        if not user:
            raise BusinessException(message="User not found")

        tweet: Tweet | None = await self.tweet_repository.find_by(id=find_tweet.id, user_id=find_tweet.user_id)

        if not tweet:
            raise BusinessException(message="Tweet not found")

        return tweet
