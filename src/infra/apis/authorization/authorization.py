from http import HTTPStatus
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from src.domain.entities.user import UserData
from src.domain.use_cases.token.decode import DecodeTokenUseCase
from src.infra.container import get_decode_token_use_case

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user_by_token(
    token: str = Depends(oauth2_scheme), decode_token_use_case: DecodeTokenUseCase = Depends(get_decode_token_use_case)
) -> UserData:
    unauthorized_exception = HTTPException(status_code=HTTPStatus.UNAUTHORIZED)

    if not token:
        raise unauthorized_exception
    try:
        user_data = await decode_token_use_case.execute(token=token)

        return UserData(**user_data)
    except Exception as exc:
        print(exc)
        raise unauthorized_exception
