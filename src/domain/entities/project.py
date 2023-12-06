from pydantic import BaseModel


class Project(BaseModel):
    id: str
    user_id: str
    name: str
