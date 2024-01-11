from typing import Annotated
from fastapi import APIRouter, Depends, status
from src.domain.dtos.user.user_data import CreateUser, UserData
from src.domain.usecases.user import ListUsersUseCase, CreateUserUseCase
from src.infrastructure.container import get_list_users_usecase, get_create_user_usecase

router = APIRouter()


@router.get("/users", response_model=list[UserData], status_code=status.HTTP_200_OK)
async def list_user(
    list_users_usecase: Annotated[ListUsersUseCase, Depends(get_list_users_usecase)],
):
    return await list_users_usecase.execute()


@router.post("/users", response_model=UserData, status_code=status.HTTP_201_CREATED)
async def create_user(
    create_users_usecase: Annotated[CreateUserUseCase, Depends(get_create_user_usecase)],
    user: CreateUser,
):
    return await create_users_usecase.execute(user=user)