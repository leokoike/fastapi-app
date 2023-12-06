from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities import Todo
from src.domain.repositories import TodoRepository
from src.infrastructure.models import TodoModel


class PgTodoRepository(TodoRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def list_by(self, project_id: str) -> list[Todo]:
        result = await self.session.stream_scalars(
            select(TodoModel).where(TodoModel.project_id == project_id).order_by(TodoModel.id)
        )

        return [todo.toEntity() async for todo in result]

    async def get_by(self, id: str) -> Todo | None:
        todo: TodoModel | None = await self.session.scalar(select(TodoModel).where(TodoModel.id == id))

        if todo:
            return todo.toEntity()
        return None

    async def save(self, todo: Todo) -> None:
        todo_data = TodoModel(**todo.model_dump())
        try:
            await self.session.merge(todo_data)
        except Exception as e:
            raise e
