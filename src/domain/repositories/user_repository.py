from abc import abstractmethod
from src.domain.entities import User


class UserRepository:
    @abstractmethod
    async def find_by(self, **kwargs) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, user: User) -> None:
        raise NotImplementedError()
