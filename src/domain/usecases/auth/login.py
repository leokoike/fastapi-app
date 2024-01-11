from src.domain.repositories.user_repository import UserRepository
from src.domain.security.data_crypto import DataCrypto
from src.domain.security.token import TokenResolver
from src.domain.dtos.login.login_data import Token

TOKEN_TYPE = "Bearer"


class LoginUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        data_crypto: DataCrypto,
        token_resolver: TokenResolver,
    ) -> None:
        self.user_repository = user_repository
        self.data_crypto = data_crypto
        self.token_resolver = token_resolver

    async def execute(
        self,
        username: str,
        password: str,
    ) -> Token:
        user = await self.user_repository.find_by(username=username)

        if not user or not user.password:
            raise Exception

        self.data_crypto.compare_value(password, user.password)

        token = self.token_resolver.generate_token(
            data={
                "id": user.id,
                "username": user.username,
            }
        )

        return Token(access_token=token, token_type=TOKEN_TYPE)
