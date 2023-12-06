from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str
    DATABASE_NAME: str


settings = Settings()
