from abc import ABC, abstractmethod
from src.domain.entities import User


class UserRepository(ABC):
    @abstractmethod
    async def find_by(self, id: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def list_all(self) -> list[User]:
        raise NotImplementedError
