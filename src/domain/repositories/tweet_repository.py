from abc import abstractmethod
from src.domain.entities import Tweet


class TweetRepository:
    @abstractmethod
    async def list_by(self, **kwargs) -> list[Tweet]:
        raise NotImplementedError()

    @abstractmethod
    async def find_by(self, **kwargs) -> Tweet:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, tweet: Tweet) -> None:
        raise NotImplementedError()
