from datetime import UTC, datetime, timedelta
import jwt

from src.infra.config import settings


class CreateTokenUseCase:
    def __init__(self):
        pass

    async def execute(self, data: dict) -> str:
        data_to_encrypt = data.copy()
        expire = datetime.now(UTC) + timedelta(minutes=settings.expire_token)
        data_to_encrypt.update({"exp": expire})

        return jwt.encode(
            data_to_encrypt,
            settings.secret_key,
            algorithm=settings.token_algorithm,
        )
