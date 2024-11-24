from src.domain.repositories import TweetRepository


class CreateTweetUseCase:
    def __init__(self, tweet_repository: TweetRepository) -> None:
        self.tweet_repository = tweet_repository
