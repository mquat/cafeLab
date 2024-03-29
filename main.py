from fastapi import FastAPI

from utils import config

from routers.router import api_router
from scheduler.scheduler import scheduler

app = FastAPI()

app.include_router(api_router)

def get_settings():
    return config.settings

scheduler.start()

