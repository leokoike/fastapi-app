from datetime import datetime, UTC
from domain.dtos import CreateUser
from domain.entities import User
from domain.repositories import UserRepository
from domain.utils.errors import BusinessException


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, new_user_data: CreateUser) -> None:
        user: User = await self.user_repository.find_by(
            username=new_user_data.username.lower().strip()
        )

        if user:
            raise BusinessException(message="username already exists")
        now = datetime.now(UTC)
        new_user = User(
            created_at=now,
            updated_at=now,
            username=new_user_data.username.lower().strip(),
            fullname=new_user_data.fullname,
            email=new_user_data.email,
            password=new_user_data.password,
        )

        await self.user_repository.create(new_user)
