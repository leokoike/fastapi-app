import sqlalchemy as sa
from src.infrastructure.database import Base
from src.domain.entities import User


class UserModel(Base):
    __tablename__ = "users"

    id: int = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
    )
    username: str = sa.Column(sa.String)
    email: str = sa.Column(sa.String)
    password: str = sa.Column(sa.String)

    def toEntity(self) -> User:
        return User(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
        )
