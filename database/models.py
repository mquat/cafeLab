from enum import Enum as enum_type

from sqlalchemy     import Table, MetaData, Column, Integer, Enum, String, Boolean, DateTime
from sqlalchemy.sql import func, expression
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()

metadata = MetaData()


class UserType(enum_type):
    user    = '회원'
    manager = '관리자'


user = Table('user', metadata,
            Column('id', Integer, primary_key=True),
            Column('username', String(255), nullable=False, unique=True),
            Column('password', String(255), nullable=False),
            Column('name', String(20), nullable=False),
            Column('registration_no', String(20), nullable=False),
            Column('address', String(255), nullable=False),
            Column('phone', String(15), nullable=False, unique=True),
            Column('email', String(255), nullable=False, unique=True),
            Column('user_type', Enum(UserType), nullable=False, server_default='user'),
            Column('joined_at', DateTime, nullable=False, server_default=func.now()),
            Column('is_deleted',Boolean, nullable=False, server_default=expression.false())
    )


class User(object):
    def __init__(self, id, username, password, name, registration_no, address, phone, email, user_type, joined_at, is_deleted):
        self.id              = id
        self.username        = username
        self.password        = password
        self.name            = name
        self.registration_no = registration_no
        self.address         = address
        self.phone           = phone
        self.email           = email
        self.user_type       = user_type
        self.joined_at       = joined_at
        self.is_deleted      = is_deleted

cafe = Table('cafe', metadata,
            Column('id', Integer, primary_key=True),
            Column('cafename', String(255), nullable=False),
            Column('address', String(255), nullable=False),
            Column('phone', String(15), nullable=False, unique=True),
            Column('lat', Integer, nullable=False),
            Column('lng', Integer, nullable=False),
            Column('parking', Boolean, nullable=False, server_default=expression.false()),
            Column('wifi', Boolean, nullable=False, server_default=expression.false()),
            Column('animal', Boolean, nullable=False, server_default=expression.false()),
            Column('wheelchair', Boolean, nullable=False, server_default=expression.false())
    )

class Cafe(object):
    def __init__(self, id, cafename, address, phone, lat, lng, parking, wifi, animal, wheelchair):
        self.id         = id
        self.cafename   = cafename
        self.address    = address
        self.phone      = phone
        self.lat        = lat
        self.lng        = lng
        self.parking    = parking
        self.wifi       = wifi
        self.animal     = animal
        self.wheelchair = wheelchair

mapper_registry.map_imperatively(User, user)
mapper_registry.map_imperatively(Cafe, cafe)

