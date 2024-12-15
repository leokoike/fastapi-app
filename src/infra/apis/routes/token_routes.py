from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.domain.dtos import Authenticate, Token
from src.domain.entities import UserData
from src.domain.use_cases import AuthenticateUseCase, CreateTokenUseCase
from src.domain.utils.errors import BusinessException
from src.infra.apis.authorization.authorization import get_user_by_token
from src.infra.container import get_authenticate_use_case, get_create_token_use_case


token_router = APIRouter()


@token_router.post("/token", response_model=Token)
async def authenticate(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_use_case: AuthenticateUseCase = Depends(get_authenticate_use_case),
    token_generator: CreateTokenUseCase = Depends(get_create_token_use_case),
):
    try:
        username, password = form_data.username, form_data.password

        user_data = await auth_use_case.execute(
            Authenticate(
                username=username,
                password=password,
            )
        )
        token = await token_generator.execute(data=user_data.model_dump())

        return Token(access_token=token)
    except BusinessException as exc:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail=exc.message)


@token_router.post("/token/user", response_model=UserData)
async def get_user(user: UserData = Depends(get_user_by_token)):
    return user
