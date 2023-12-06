from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str | None
    email: str | None
