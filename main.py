from fastapi import FastAPI

from utils import config

app = FastAPI()

def get_settings():
    return config.settings


