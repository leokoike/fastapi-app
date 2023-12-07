from pydantic import BaseModel


class Project(BaseModel):
    id: int | None
    user_id: int
    name: str
