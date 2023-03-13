from fastapi import FastAPI

from database import models, session

models.Base.metadata.create_all(bind=session.engine)

app = FastAPI()
