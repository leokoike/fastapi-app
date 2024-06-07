from datetime import datetime
from pydantic import BaseModel


class AuditData(BaseModel):
    created_at: datetime
    updated_at: datetime
