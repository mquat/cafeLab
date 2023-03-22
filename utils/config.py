import os

from pydantic import BaseSettings
from typing import Union

class Settings(BaseSettings):
    mysql_username : str = os.getenv("DB_USERNAME")
    mysql_password : Union[str, int] = os.getenv("DB_PASSWORD")
    mysql_host     : str = os.getenv("DB_HOST")
    mysql_port     : str = os.getenv("DB_PORT")
    mysql_database : str = os.getenv("DB_DATABASE")

    database_url = f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}?charset=utf8"

    class Config:
        env_file = ".env"

settings = Settings()

