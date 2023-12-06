import sqlalchemy as sa
from src.infrastructure.database import Base
from src.domain.entities import Project


class ProjectModel(Base):
    __tablename__ = "projects"

    id: str = sa.Column(sa.UUID, primary_key=True)  # type: ignore
    user_id: str = sa.Column(sa.ForeignKey("users.id"))
    name: str = sa.Column(sa.String)

    def toEntity(self) -> Project:
        return Project(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
        )
