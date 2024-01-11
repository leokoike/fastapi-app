from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities import Project
from src.domain.repositories import ProjectRepository
from src.infrastructure.models import ProjectModel


class PgProjectRespository(ProjectRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def list_by(self, user_id: str) -> list[Project]:
        result = await self.session.stream_scalars(
            select(ProjectModel).where(ProjectModel.user_id == user_id).order_by(ProjectModel.name)
        )

        return [project.toEntity() async for project in result]

    async def get_by(self, id: str) -> Project | None:
        project: ProjectModel | None = await self.session.scalar(select(ProjectModel).where(ProjectModel.id == id))

        if project:
            return project.toEntity()

        return None

    async def save(self, project: Project) -> None:
        project_data = ProjectModel(**project.model_dump())
        try:
            await self.session.merge(project_data)
        except Exception as e:
            raise e
