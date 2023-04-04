from pydantic import BaseModel, constr
from typing import Union

class createUser(BaseModel):
    username: constr(regex='/^[A-Za-z0-9]*$/')
    password: str(regex='/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/')
    name: str
    registration_no: str
    address: str
    phone: str
    email: constr(regex='/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/')
    user_type: Union[str, None] = None

