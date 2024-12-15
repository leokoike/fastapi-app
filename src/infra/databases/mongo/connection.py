from src.infra.config import settings
from pymongo import AsyncMongoClient


class MongoConnection:
    client: AsyncMongoClient = None

    @classmethod
    async def create_db_connection(cls):
        cls.client = AsyncMongoClient(
            settings.database_uri,
        )

    @classmethod
    async def close_db_connection(cls):
        if cls.client:
            await cls.client.close()

    @classmethod
    async def is_db_connected(cls) -> bool:
        return bool(await cls.client.server_info())
