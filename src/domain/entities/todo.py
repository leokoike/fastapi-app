from pydantic import BaseModel


class Todo(BaseModel):
    id: str
    project_id: str
    description: str
