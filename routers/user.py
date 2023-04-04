from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db

from router import router

from schemas.user import createUser

from crud.user import (
    create_user,
    get_duplicate_user
)

router = APIRouter()

@router.post("/signup", status_code=201)
def signup(
    signup_info: createUser,
    db: Session = Depends(get_db)
):

    duplicate_user = get_duplicate_user(signup_info.username, db)
    if duplicate_user:
        raise HTTPException(status_code=209, detail='이미 존재하는 사용자입니다')

    try:
        create_user(signup_info, db)

    except:
        raise HTTPException(status_code=400, detail='재시도해주세요')
    
    return {'message': 'SIGNUP SUCCESS!'}

