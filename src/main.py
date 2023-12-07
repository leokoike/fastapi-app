from fastapi import FastAPI, Request, Response
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import user_router
from src.infrastructure.database import sessionmaker
from sqlalchemy.ext.asyncio import async_scoped_session


app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    prefix="/api/v1",
    router=user_router,
    tags=["User"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        from asyncio import current_task

        AsyncScopedSession = async_scoped_session(
            sessionmaker,
            scopefunc=current_task,
        )
        request.state.session = AsyncScopedSession()
        response = await call_next(request)
    finally:
        await AsyncScopedSession.remove()
    return response


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"status": "ok"}
