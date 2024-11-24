from src.domain.entities.base import AuditData


class Tweet(AuditData):
    id: str
    user_id: str
    content: str
