import sqlalchemy as sa
from src.infrastructure.database import Base
from src.domain.entities import Project


class ProjectModel(Base):
    __tablename__ = "projects"

    id: int = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id: int = sa.Column(sa.ForeignKey("users.id"))
    name: str = sa.Column(sa.String)

    def toEntity(self) -> Project:
        return Project(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
        )
