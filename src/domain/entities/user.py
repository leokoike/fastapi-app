from src.domain.entities.base import AuditData


class User(AuditData):
    id: str | None = None
    username: str
    fullname: str
    email: str
    password: str
