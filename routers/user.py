from fastapi import APIRouter, Depends, HTTPException

from database.session import get_db

from schemas.user import createUser

from utils.auth import get_password_hash

from crud.user import (
    create_user,
    get_duplicate_user
)

router = APIRouter()

db = Depends(get_db)

@router.post("/signup", status_code=201)
def signup(
    signup_info: createUser,
    db = db
):
    duplicate_user = get_duplicate_user(signup_info, db)
    if duplicate_user:
        raise HTTPException(status_code=400, detail='이미 존재하는 사용자입니다')

    try:
        hashed_password = get_password_hash(signup_info.password)
        signup_info.password = hashed_password
        create_user(signup_info, db)
    except:
        raise HTTPException(status_code=400, detail='재시도해주세요')
    
    return {'message': 'SIGNUP SUCCESS!'}


