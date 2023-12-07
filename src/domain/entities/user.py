from pydantic import BaseModel


class User(BaseModel):
    id: int | None
    name: str | None
    email: str | None
