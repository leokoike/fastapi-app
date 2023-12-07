from src.domain.entities import User
from src.domain.repositories import UserRepository


class ListUsersUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self) -> list[dict]:
        users: list[User] = await self.user_repository.list_all()

        return [user.model_dump() for user in users]
