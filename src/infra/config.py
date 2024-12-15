from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["settings"]


class Settings(BaseSettings):
    """
    Class that stores global values for the application.
    """

    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    server_host: str = "0.0.0.0"
    server_port: int = 8000
    log_level: str = "INFO"
    debug: bool = False
    reload: bool = False

    # MongoDB
    database_uri: str = "mongodb://root:toor@localhost:27017"
    database_name: str = "fakeTwitter"
    users_collection: str = "users"
    tweets_collection: str = "tweets"

    # JWT
    secret_key: str = "super-secret"
    expire_token: int = 30
    algorithm_encode: str = "HS256"


settings = Settings()
