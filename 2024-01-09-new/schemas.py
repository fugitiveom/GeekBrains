from datetime import datetime

from pydantic import BaseModel, PositiveFloat, EmailStr, SecretStr
from typing_extensions import Optional


class GoodsWrite(BaseModel):
    name: str
    desc: str
    price: PositiveFloat


class OrdersWrite(BaseModel):
    users: int
    goods: int


class UsersWrite(BaseModel):
    name: str
    surname: str
    email: EmailStr
    hashed_password: str


class GoodsRead(BaseModel):
    id: int
    name: str
    desc: str
    price: PositiveFloat


class UsersRead(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    hashed_password: SecretStr


class OrdersRead(BaseModel):
    id: int
    goods: Optional[int]
    users: Optional[int]
    created: datetime
    status: int
