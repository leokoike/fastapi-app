from src.domain.dtos.user.user_data import UserData
from src.domain.entities import User
from src.domain.repositories import UserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, user: UserData) -> User:
        new_user = await self.user_repository.save(user=user)

        return new_user
