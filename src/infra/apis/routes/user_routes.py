from fastapi import APIRouter, Depends

from src.domain.dtos import CreateUser
from src.domain.use_cases import CreateUserUseCase
from src.infra.container import get_create_user_use_case

user_router = APIRouter()


@user_router.post("/users/")
async def create_user(
    user_data: CreateUser,
    use_case: CreateUserUseCase = Depends(get_create_user_use_case),
):
    return await use_case.execute(new_user_data=user_data)
