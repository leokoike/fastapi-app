import jwt

from src.infrastructure.config import settings
from src.domain.security.token import TokenResolver

ALGORITHM = "HS256"


class JWTTokenResolver(TokenResolver):
    def generate_token(self, data: dict) -> str:
        return jwt.encode(
            payload=data,
            key=settings.SECRET_KEY,
            algorithm=ALGORITHM,
        )

    def decode_token(self, token: str) -> dict:
        return jwt.decode(
            jwt=token,
            key=settings.SECRET_KEY,
            algorithms=[ALGORITHM],
        )
