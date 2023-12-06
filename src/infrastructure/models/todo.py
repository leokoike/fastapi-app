import sqlalchemy as sa
from src.infrastructure.database import Base
from src.domain.entities import Todo


class TodoModel(Base):
    __tablename__ = "todos"

    id: str = sa.Column(sa.UUID, primary_key=True)  # type: ignore
    project_id: str = sa.Column(sa.ForeignKey("projects.id"))
    description: str = sa.Column(sa.String)

    def toEntity(self) -> Todo:
        return Todo(
            id=self.id,
            project_id=self.project_id,
            description=self.description,
        )
