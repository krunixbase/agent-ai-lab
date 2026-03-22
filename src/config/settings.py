from pydantic import BaseSettings, Field
from functools import lru_cache

class Settings(BaseSettings):
    # LLM configuration
    OPENAI_API_KEY: str | None = Field(default=None)
    OPENAI_MODEL: str = Field(default="gpt-4.1")

    # Vector DB
    VECTOR_DB_PROVIDER: str = Field(default="chroma")
    VECTOR_DB_PATH: str = Field(default="./vector_store")

    # Server
    SERVER_HOST: str = Field(default="0.0.0.0")
    SERVER_PORT: int = Field(default=8000)

    # Logging
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FORMAT: str = Field(default="json")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
