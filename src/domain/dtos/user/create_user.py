from pydantic import BaseModel


class CreateUser(BaseModel):
    fullname: str
    username: str
    email: str
    password: str
