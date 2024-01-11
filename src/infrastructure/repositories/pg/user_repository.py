from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.dtos.user.user_data import CreateUser, UserData
from src.domain.entities import User
from src.domain.repositories import UserRepository
from src.infrastructure.models import UserModel


class PgUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def find_by(self, username: str) -> User | None:
        user: UserModel | None = await self.session.scalar(
            select(UserModel).where(UserModel.username == username),
        )
        if user:
            return user.toEntity()
        return None

    async def save(self, user: CreateUser) -> User:
        user_data = UserModel(**user.model_dump())

        res = await self.session.merge(user_data)
        await self.session.flush([res])
        return res.toEntity()

    async def list_all(self) -> list[UserData]:
        result = await self.session.stream_scalars(
            select(UserModel.id, UserModel.username, UserModel.email).order_by(UserModel.username)
        )

        return [
            UserData(
                id=user.id,
                username=user.username,
                email=user.email,
            )
            async for user in result
        ]
