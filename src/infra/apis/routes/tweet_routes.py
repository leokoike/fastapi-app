from fastapi import APIRouter, Depends
from src.domain.dtos import CreateTweet, FindTweet
from src.domain.use_cases import CreateTweetUseCase, FindTweetUseCase
from src.infra.container import get_create_tweet_use_case, get_find_tweet_use_case


tweet_router = APIRouter()


@tweet_router.post("/tweet/")
async def create_tweet(tweet_data: CreateTweet, use_case: CreateTweetUseCase = Depends(get_create_tweet_use_case)):
    return await use_case.execute(create_tweet=tweet_data)


@tweet_router.get("/tweet/{id}/")
async def find_tweet(id: str, user_id: str, use_case: FindTweetUseCase = Depends(get_find_tweet_use_case)):
    return await use_case.execute(find_tweet=FindTweet(id=id, user_id=user_id))
