from pydantic import BaseModel


class Todo(BaseModel):
    id: int | None
    project_id: int
    description: str
