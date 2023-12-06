from abc import ABC, abstractmethod

from src.domain.entities import Todo


class TodoRepository(ABC):
    @abstractmethod
    async def list_by(self, project_id: str) -> list[Todo]:
        raise NotImplementedError

    @abstractmethod
    async def get_by(self, id: str) -> Todo | None:
        raise NotImplementedError

    @abstractmethod
    async def save(self, todo: Todo) -> None:
        raise NotImplementedError
