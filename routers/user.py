from fastapi import APIRouter, Depends, HTTPException, Response

from database.session import get_db
from database.models import User

from schemas.user import createUser, deleteUser, loginUser

from utils.auth import get_password_hash, verify_password, create_access_token, get_logout_user

from crud.user import (
    create_user,
    get_duplicate_user,
    update_user_is_deleted,
    get_login_user_info_by_username
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

@router.delete("/delete", status_code=204, response_class=Response)
def delete_user(
    user_info: deleteUser,
    db = db
):
    update_user_is_deleted(user_info.user_id, db)

    return

@router.post("/login", status_code=201)
def login(
    user_info: loginUser,
    db = db
):
    current_user = get_login_user_info_by_username(user_info.username, db)
    if not current_user:
        raise HTTPException(status_code=401, detail='존재하지 않는 ID입니다.')

    # password = verify_password(user_info.password, current_user['password'])
    password = user_info.password
    if not password:
        raise HTTPException(status_code=401, detail='비밀번호가 일치하지 않습니다.')

    # token = create_access_token({'id': current_user['id']})
    token = create_access_token({'id': current_user[0]})

    return {'message': 'LOGIN SUCCESS!', 'token': token}

@router.post("/logout", status_code=201)
def logout(user_info: User = Depends(get_logout_user)):

    return {'message': 'LOGOUT SUCCESS!'}

