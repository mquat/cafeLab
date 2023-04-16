from sqlalchemy import or_, update
from sqlalchemy.orm import Session

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

