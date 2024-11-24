from pydantic import BaseModel


class FindTweet(BaseModel):
    id: str
    user_id: str
