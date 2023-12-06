from abc import ABC, abstractmethod

from src.domain.entities import Project


class ProjectRepository(ABC):
    @abstractmethod
    async def list_by(self, user_id: str) -> list[Project]:
        raise NotImplementedError

    @abstractmethod
    async def get_by(self, id: str) -> Project | None:
        raise NotImplementedError

    @abstractmethod
    async def save(self, project: Project) -> None:
        raise NotImplementedError
