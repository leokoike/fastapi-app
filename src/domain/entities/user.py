from pydantic import BaseModel
from src.domain.entities.base import AuditData


class UserData(BaseModel):
    id: str | None = None
    username: str
    fullname: str
    email: str


class User(UserData, AuditData):
    password: str
