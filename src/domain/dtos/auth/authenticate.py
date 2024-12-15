from pydantic import BaseModel


class Authenticate(BaseModel):
    username: str
    password: str
