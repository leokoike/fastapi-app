from src.domain.dtos.user.user_data import UserData
from src.domain.repositories import UserRepository


class ListUsersUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self) -> list[UserData]:
        users: list[UserData] = await self.user_repository.list_all()

        return users
