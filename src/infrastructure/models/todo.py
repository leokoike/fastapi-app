import sqlalchemy as sa
from src.infrastructure.database import Base
from src.domain.entities import Todo


class TodoModel(Base):
    __tablename__ = "todos"

    id: int = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
    )
    project_id: int = sa.Column(sa.ForeignKey("projects.id"))
    description: str = sa.Column(sa.String)

    def toEntity(self) -> Todo:
        return Todo(
            id=self.id,
            project_id=self.project_id,
            description=self.description,
        )
