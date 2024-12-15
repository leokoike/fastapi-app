from pymongo.asynchronous.client_session import AsyncClientSession
from src.infra.databases.mongo.connection import MongoConnection


class MongoSession:
    def __init__(self) -> None:
        self.session: AsyncClientSession = None

    async def __aenter__(self) -> AsyncClientSession:
        self.session = MongoConnection.client.start_session()
        return self.session

    async def __aexit__(self, exc_type, exc_val, traceback) -> None:
        await self.session.end_session()
