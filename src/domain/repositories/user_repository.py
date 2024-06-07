from abc import abstractmethod
from domain.entities import User


class UserRepository:

    @abstractmethod
    async def find_by(self, id: str = None, username: str = None) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, user: User) -> None:
        raise NotImplementedError()
