import os
import redis

from dotenv import load_dotenv

from pydantic import BaseSettings

from typing import Optional

load_dotenv(verbose=True)

class Settings(BaseSettings):
    mysql_username : Optional[str] = os.getenv("DB_USERNAME")
    mysql_password : Optional[str] = os.getenv("DB_PASSWORD")
    mysql_host     : Optional[str] = os.getenv("DB_HOST")
    mysql_port     : Optional[str] = os.getenv("DB_PORT")
    mysql_database : Optional[str] = os.getenv("DB_DATABASE")
    secret_key     : Optional[str] = os.getenv("SECRET_KEY")
    algorithm      : Optional[str] = os.getenv("ALGORITHM")
    redis_host     : Optional[str] = os.getenv("REDIS_HOST")
    redis_port     : Optional[str] = os.getenv("REDIS_PORT")
    redis_database : Optional[str] = os.getenv("REDIS_DATABASE")
    kakao_api_key  : Optional[str] = os.getenv("KAKAO_API_KEY")
    google_api_key : Optional[str] = os.getenv("GOOGLE_API_KEY")

    database_url = f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}:3306/{mysql_database}?charset=utf8"

    class Config:
        env_file = ".env"

settings = Settings()

def load_redis():
    return redis.Redis(
        host = settings.redis_host,
        port = settings.redis_port,
        db   = settings.redis_database
    )

