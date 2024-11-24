from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClientSession

from src.infra.databases.mongo.connection import MongoConnection


async def get_conn(request: Request) -> MongoConnection:
    return request.state.conn


async def get_session(request: Request) -> AsyncIOMotorClientSession:
    return request.state.session
