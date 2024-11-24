from pydantic import BaseModel


class CreateTweet(BaseModel):
    user_id: str
    content: str
