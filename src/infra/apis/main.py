from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends
from src.infra.container import get_conn
from src.infra.databases.mongo.connection import MongoConnection
from src.infra.databases.mongo.session import MongoSession


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await startup(app)
        yield
    finally:
        await shutdown(app)


async def startup(app: FastAPI):
    await MongoConnection.create_db_connection()


async def shutdown(app: FastAPI):
    await MongoConnection.close_db_connection()


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def http_session_db(request: Request, call_next):
    request.state.conn = MongoConnection
    async with MongoSession() as session:
        request.state.session = session
        response = await call_next(request)
    return response


@app.get("/")
async def health(db: MongoConnection = Depends(get_conn)):
    return {"api": "ok", "db": await db.is_db_connected()}
