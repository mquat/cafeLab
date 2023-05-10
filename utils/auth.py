from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt
from typing import Union
from fastapi import Depends, HTTPException, Header, status

from .config import settings, load_redis
from database.session import get_db
from crud.user import get_user_payload_by_token, delete_authorization_token

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db = Depends(get_db)
ALGORITHM = 'HS256'
redis = load_redis()

credentials_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = 'INVALID TOKEN',
    headers = {'WWW-Authenticate': 'Bearer'}
)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(payload:dict) -> str:
    expire = datetime.utcnow() + timedelta(days=3)
    payload.update({'exp': expire})
    encoded_jwt = jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)

    return encoded_jwt

def get_logout_user(authorization : Union[str, None] = Header(default=None), db = db):
    if not authorization:
        raise credentials_exception

    if redis.get(authorization):
        raise credentials_exception

    user_payload = get_user_payload_by_token(authorization, db)
    delete_authorization_token(authorization, user_payload)

    return

