from fastapi import FastAPI, Request, Response, status
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.api.routes import user_router
from src.infrastructure.database import AsyncScopedSession
from sqlalchemy.ext.asyncio import AsyncSession


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


# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-middleware
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        session: AsyncSession = AsyncScopedSession()
        request.state.session = session
        response = await call_next(request)
    finally:
        if response.status_code >= status.HTTP_400_BAD_REQUEST:
            await session.rollback()
        else:
            await session.commit()
        await AsyncScopedSession.remove()
    return response


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"status": "ok"}
