from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities import User
from src.domain.repositories import UserRepository
from src.infrastructure.models import UserModel


class PgUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def find_by(self, id: str) -> User | None:
        user: UserModel | None = await self.session.scalar(select(UserModel).where(UserModel.id == id))

        if user:
            return user.toEntity()

        return None

    async def save(self, user: User) -> None:
        user_data = UserModel(**user.model_dump())
        try:
            await self.session.merge(user_data)
        except Exception as e:
            raise e

    async def list_all(self) -> list[User]:
        result = await self.session.stream_scalars(select(UserModel).order_by(UserModel.name))

        return [user.toEntity() async for user in result]
