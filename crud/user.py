from sqlalchemy import or_, update, and_
from sqlalchemy.orm import Session
from typing import Union

from schemas.user import createUser
from database.models import User

def create_user(
    signup_info: createUser,
    db: Session
) -> User:

    db_obj = User(
        id              =signup_info.id,
        username        = signup_info.username,
        password        = signup_info.password,
        name            = signup_info.name,
        registration_no = signup_info.registration_no,
        address         = signup_info.address,
        phone           = signup_info.phone,
        email           = signup_info.email,
        user_type       = signup_info.user_type,
        joined_at       = signup_info.joined_at,
        is_deleted      = signup_info.is_deleted
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

def get_duplicate_user(
    signup_info: createUser,
    db: Session
)-> bool:
    user = db.query(User).filter(
                            or_(
                            User.username == signup_info.username,
                            User.email == signup_info.email,
                            User.phone == signup_info.phone)
                        ).first()

    if user:
        return True
    return False

def delete_user(
    user_id: int, 
    db: Session
)-> None:
    db.execute(update(User).where(User.id == user_id).values(is_deleted=True))

    db.commit()

    return

def get_valid_user(
    user_info: dict,
    db: Session
)-> bool:
    user = db.query(User).where(
        and_(
            User.username == user_info['username'],
            User.password == user_info['password'],
            User.is_deleted == 0
            )
        ).first()

    if user:
        return True
    return False

def get_user_login_info_by_username(
    username: str,
    db: Session
)-> Union[tuple, bool]:
    user = db.query(User).with_entities(
                            User.username,
                            User.password
                        ).where(
                            User.username == username,
                            User.is_deleted == False
                        ).first()

    if user:
        return user
    return False

