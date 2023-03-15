import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    mysql_username : str = os.getenv("DB_USERNAME")
    mysql_password       = os.getenv("DB_PASSWORD")
    mysql_host     : str = os.getenv("DB_HOST")
    mysql_port     : str = os.getenv("DB_PORT")
    mysql_database : str = os.getenv("DB_DATABASE")

    database_url = f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}?charset=utf8"

settings = Settings()
