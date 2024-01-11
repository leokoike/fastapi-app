from pydantic import BaseModel


class User(BaseModel):
    id: int | None
    username: str | None
    email: str | None
    password: str | None
