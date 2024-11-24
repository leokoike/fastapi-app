from src.infra.config import settings
from motor.motor_asyncio import AsyncIOMotorClient


class MongoConnection:
    client: AsyncIOMotorClient = None

    @classmethod
    async def create_db_connection(cls):
        cls.client = AsyncIOMotorClient(
            settings.database_uri,
        )

    @classmethod
    async def close_db_connection(cls):
        if cls.client:
            cls.client.close()

    @classmethod
    async def is_db_connected(cls) -> bool:
        return bool(await cls.client.server_info())
