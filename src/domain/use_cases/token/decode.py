from datetime import UTC, datetime
import jwt

from src.domain.utils.errors import BusinessException
from src.infra.config import settings


class DecodeTokenUseCase:
    def __init__(self):
        pass

    async def execute(self, token: str) -> dict:
        data: dict = jwt.decode(jwt=token, key=settings.secret_key, algorithms=[settings.algorithm_encode])

        date_exp = datetime.fromtimestamp(data["exp"], tz=UTC)
        if date_exp < datetime.now(UTC):
            raise BusinessException("Token expired")

        return data
