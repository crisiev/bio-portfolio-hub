"""Core configuration settings for Thesis Stat Assistant."""

from pydantic import BaseModel


class Settings(BaseModel):
    PROJECT_NAME: str = "Thesis Stat Assistant"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"


settings = Settings()
