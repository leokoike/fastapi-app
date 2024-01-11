from src.domain.security.data_crypto import DataCrypto
from src.domain.dtos.user.user_data import CreateUser, UserData
from src.domain.repositories import UserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository, data_crypto: DataCrypto) -> None:
        self.user_repository = user_repository
        self.data_crypto = data_crypto

    async def execute(self, user: CreateUser) -> UserData:
        # validate username
        if await self.user_repository.find_by(username=user.username):
            raise Exception

        user.password = self.data_crypto.encrypt_data(data=user.password)
        new_user = await self.user_repository.save(user=user)

        return UserData(
            id=new_user.id,
            username=new_user.username,
            email=new_user.email,
        )
