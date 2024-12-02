from datetime import datetime, UTC
from src.domain.dtos import CreateUser
from src.domain.entities import User
from src.domain.repositories import UserRepository
from src.domain.utils.errors import BusinessException
from src.domain.utils.security import HashingData


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository, hashing_data: HashingData) -> None:
        self.user_repository = user_repository
        self.hashing_data = hashing_data

    async def execute(self, new_user_data: CreateUser) -> None:
        username = new_user_data.username.lower().strip()
        user: User | None = await self.user_repository.find_by(
            username=username,
        )
        if user:
            raise BusinessException(message="username already exists")
        now = datetime.now(UTC)

        hashed_password = self.hashing_data.get_hashed_data(new_user_data.password)
        new_user = User(
            created_at=now,
            updated_at=now,
            username=username,
            fullname=new_user_data.fullname,
            email=new_user_data.email,
            password=hashed_password,
        )

        await self.user_repository.create(new_user)
