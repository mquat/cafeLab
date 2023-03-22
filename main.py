from functools import lru_cache
from fastapi import FastAPI

from utils import config

app = FastAPI()

@lru_cache
def get_settings():
    return config.settings

get_settings()