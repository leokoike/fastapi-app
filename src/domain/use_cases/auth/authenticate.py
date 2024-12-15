from src.domain.utils.errors import BusinessException
from src.domain.dtos import Authenticate
from src.domain.entities import UserData, User
from src.domain.repositories import UserRepository
from src.domain.utils.security import HashingData


class AuthenticateUseCase:
    def __init__(self, user_repository: UserRepository, hashing_data: HashingData):
        self.user_repository = user_repository
        self.hashing_data = hashing_data

    async def execute(self, authenticate: Authenticate) -> UserData:
        username = authenticate.username.lower().strip()
        user: User | None = await self.user_repository.find_by(username=username)

        if not user or not self.hashing_data.validate_data(authenticate.password, user.password):
            raise BusinessException("Authentication failed.")

        return UserData(**user.model_dump())
