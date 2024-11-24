from src.domain.entities.base import AuditData


class Tweet(AuditData):
    id: str | None = None
    user_id: str
    content: str
