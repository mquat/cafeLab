from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt
from fastapi import Depends

from .config import settings
from database.session import get_db

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db = Depends(get_db)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(payload:dict) -> str:
    expire = datetime.utcnow() + timedelta(days=int(settings.expire_days))
    payload.update({'exp': expire})
    encoded_jwt = jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

    return encoded_jwt

