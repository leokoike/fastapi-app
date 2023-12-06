from fastapi import APIRouter

route = APIRouter()


@route.get("/users")
def list_user():
    pass
