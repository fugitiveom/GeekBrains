from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Float, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped

from manager import Base


class Goods(Base):
    __tablename__ = "goods"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    desc: Mapped[Optional[str]] = Column(String)
    price: Mapped[float] = Column(Float)


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = Column(String)
    surname: Mapped[Optional[str]] = Column(String)
    email: str = Column(String, unique=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = Column(Integer, primary_key=True)
    created: DATETIME = Column(DATETIME, default=datetime.now)
    status: int = Column(Integer, default=0)
    goods: Mapped[int | None] = Column(Integer, ForeignKey("goods.id"), nullable=True)
    users: Mapped[int] = Column(Integer, ForeignKey("users.id"))
