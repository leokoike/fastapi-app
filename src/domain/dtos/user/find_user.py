from pydantic import BaseModel


class FindUser(BaseModel):
    username: str
