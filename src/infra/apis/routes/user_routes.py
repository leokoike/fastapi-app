from fastapi import APIRouter, Depends

from src.domain.dtos import CreateUser, FindUser
from src.domain.use_cases import CreateUserUseCase, FindUserUseCase
from src.infra.container import get_create_user_use_case, get_find_user_use_case

user_router = APIRouter()


@user_router.post("/users/")
async def create_user(
    user_data: CreateUser,
    use_case: CreateUserUseCase = Depends(get_create_user_use_case),
):
    return await use_case.execute(new_user_data=user_data)


@user_router.get("/users/{username}/")
async def find_user(
    username: str,
    use_case: FindUserUseCase = Depends(get_find_user_use_case),
):
    return await use_case.execute(find_user=FindUser(username=username))
