from src.domain.dtos import FindUser
from src.domain.entities import User, UserData
from src.domain.repositories import UserRepository
from src.domain.utils.errors import BusinessException


class FindUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, find_user: FindUser) -> UserData:
        user: User | None = await self.user_repository.find_by(
            username=find_user.username.lower().strip(),
        )
        if not user:
            raise BusinessException(message="User not found")

        return UserData(
            **user.model_dump(),
        )
