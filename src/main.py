from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.user_route import route as user_route


app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/api/v1", route=user_route)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"status": "ok"}
