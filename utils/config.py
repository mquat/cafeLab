import os

from dotenv import load_dotenv

from pydantic import BaseSettings

from typing import Union

load_dotenv(verbose=True)

class Settings(BaseSettings):
    mysql_username : str = os.getenv("DB_USERNAME")
    mysql_password : Union[str, int] = os.getenv("DB_PASSWORD")
    mysql_host     : str = os.getenv("DB_HOST")
    mysql_port     : Union[str, int] = os.getenv("DB_PORT")
    mysql_database : str = os.getenv("DB_DATABASE")

    database_url = f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}:3306/{mysql_database}?charset=utf8"

    class Config:
        env_file = ".env"

settings = Settings()

