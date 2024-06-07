from domain.entities.base import AuditData


class User(AuditData):
    id: str
    username: str
    fullname: str
    email: str
    password: str
