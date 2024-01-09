from datetime import datetime

from pydantic import BaseModel, PositiveFloat, EmailStr


class Good(BaseModel):
    name: str
    desc: str
    price: PositiveFloat


class Order(BaseModel):
    date: datetime
    status: int


class User(BaseModel):
    name: str
    surname: str
    email: EmailStr
    
