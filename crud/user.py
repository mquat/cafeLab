from sqlalchemy.orm import Session

from schemas.user import createUser

from database.models import User

from utils.auth import pwd_context

def create_user(
    signup_info: createUser,
    db: Session
) -> User:
    db_user = User(
        username        = signup_info.username,
        password        = pwd_context.hash(signup_info.password),
        name            = signup_info.name,
        registration_no = signup_info.registration_no,
        address         = signup_info.address,
        phone           = signup_info.phone,
        email           = signup_info.email,
        user_type       = signup_info.user_type
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_duplicate_user(
    signup_info: createUser,
    db: Session
):
    user = db.query(User).filter(
                            User.username == signup_info.username |
                            User.email == signup_info.email |
                            User.phone == signup_info.phone
                        ).first()

    return user

