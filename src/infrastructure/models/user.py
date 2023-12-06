import sqlalchemy as sa
from src.infrastructure.database import Base
from src.domain.entities import User


class UserModel(Base):
    __tablename__ = "users"

    id: str = sa.Column(sa.UUID, primary_key=True)  # type: ignore
    name: str = sa.Column(sa.String)
    email: str = sa.Column(sa.String)

    def toEntity(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
        )
