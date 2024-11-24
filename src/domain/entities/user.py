from src.domain.entities.base import AuditData
from bson import ObjectId


class User(AuditData):
    _id: str | ObjectId | None = None
    username: str
    fullname: str
    email: str
    password: str
