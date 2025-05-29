import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    DEBUG: bool = True
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"
