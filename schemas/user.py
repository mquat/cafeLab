import re

from pydantic import BaseModel, validator

from typing import Union

from database.models import UserType

class createUser(BaseModel):
    id: Union[int, None]
    username: str
    password: str
    name: str
    registration_no: str
    address: str
    phone: str
    email: str
    user_type: UserType
    joined_at: Union[str, None]
    is_deleted: bool

    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[A-Za-z0-9]*$', v):
            raise ValueError('유효하지 않은 양식의 ID입니다.')
        return v

    @validator('password')
    def validate_password(cls, v):
        if not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$', v):
            raise ValueError('유효하지 않은 양식의 비밀번호입니다.')
        return v

    @validator('email')
    def validate_email(cls, v):
        if not re.match(r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', v):
            raise ValueError('유효하지 않은 이메일 양식입니다.')
        return v

class deleteUser(BaseModel):
    user_id: int

class loginUser(BaseModel):
    username: str
    password: str

