from enum import Enum as enum_type

from sqlalchemy     import Column, Integer, Enum, String, Boolean, DateTime
from sqlalchemy.sql import func, expression

from .session import Base

class PrimaryKey:
    id = Column(Integer, primary_key=True, index=True, unique=True)


class UserType(enum_type):
    user    = '회원'
    manager = '관리자'


class User(Base, PrimaryKey):
    __tablename__ = 'users'

    username        = Column(String(255), nullable=False, unique=True)
    password        = Column(String(255), nullable=False)
    name            = Column(String(20), nullable=False)
    registration_no = Column(String(20), nullable=False)
    address         = Column(String(255), nullable=False)
    phone           = Column(String(15), nullable=False, unique=True)
    email           = Column(String(255), nullable=False, unique=True)
    user_type       = Column(Enum(UserType), nullable=False, server_default='user')
    joined_at       = Column(DateTime, nullable=False, server_default=func.now())
    is_deleted      = Column(Boolean(), nullable=False, server_default=expression.false())
