import os
import secrets
from dotenv import load_dotenv

from pydantic import BaseSettings, EmailStr


load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SQL_ALCHEMY_DATABASE_URL: str = os.getenv("SQL_ALCHEMY_DATABASE_URL")
    FIRST_SUPERUSER: EmailStr = os.getenv("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str = os.getenv("FIRST_SUPERUSER_PASSWORD")

    class Config:
        case_sensetive = True


settings = Settings()
