from motor.motor_asyncio import AsyncIOMotorClientSession
from src.infra.databases.mongo.connection import MongoConnection


class MongoSession:
    def __init__(self) -> None:
        self.session = None

    async def __aenter__(self) -> AsyncIOMotorClientSession:
        self.session = await MongoConnection.client.start_session()
        return self.session

    async def __aexit__(self, exc_type, exc_val, traceback) -> None:
        await self.session.end_session()
