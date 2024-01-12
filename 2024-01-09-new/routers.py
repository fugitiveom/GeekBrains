from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing_extensions import List

from manager import get_session

from schemas import UsersWrite, GoodsWrite, OrdersWrite, UsersRead, GoodsRead, OrdersRead

import services

from db import Users, Goods, Orders

router = APIRouter()


@router.post("/users")
def create_user(user_data: UsersWrite, session: Session = Depends(get_session)):
    db_user = services.obj_get_by_email(session, user_data.email, obj_class=Users)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    services.obj_create(session, user_data.model_dump(), obj_class=Users)


@router.get("/users", response_model=List[UsersRead])
def get_users(session: Session = Depends(get_session)):
    return services.obj_get(session, offset=0, limit=50, obj_class=Users)


@router.get("/users/{user_id}", response_model=UsersRead)
def get_user(user_id: int, session: Session = Depends(get_session)):
    return services.obj_get_by_id(session, user_id, obj_class=Users)


@router.patch("/users/{user_id}")
def update_user(user_id: int, user_data: UsersWrite, session: Session = Depends(get_session)):
    services.obj_update(session, user_id, user_data.model_dump(), obj_class=Users)


@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    services.obj_delete(session, user_id, obj_class=Users)


@router.post("/goods")
def create_good(good_data: GoodsWrite, session: Session = Depends(get_session)):
    services.obj_create(session, good_data.model_dump(), obj_class=Goods)


@router.get("/goods", response_model=List[GoodsRead])
def get_goods(session: Session = Depends(get_session)):
    return services.obj_get(session, offset=0, limit=50, obj_class=Goods)


@router.get("/goods/{good_id}", response_model=GoodsRead)
def get_good(good_id: int, session: Session = Depends(get_session)):
    return services.obj_get_by_id(session, good_id, obj_class=Goods)


@router.patch("/goods/{good_id}")
def update_good(good_id: int, good_data: GoodsWrite, session: Session = Depends(get_session)):
    services.obj_update(session, good_id, good_data.model_dump(), obj_class=Goods)


@router.delete("/goods/{good_id}")
def delete_good(good_id: int, session: Session = Depends(get_session)):
    services.obj_delete(session, good_id, obj_class=Goods)


@router.post("/orders")
def create_order(order_data: OrdersWrite, session: Session = Depends(get_session)):
    services.obj_create(session, order_data.model_dump(), obj_class=Orders)


@router.get("/orders", response_model=List[OrdersRead])
def get_orders(session: Session = Depends(get_session)):
    return services.obj_get(session, offset=0, limit=50, obj_class=Orders)


@router.get("/orders/{order_id}", response_model=OrdersRead)
def get_order(order_id: int, session: Session = Depends(get_session)):
    return services.obj_get_by_id(session, order_id, obj_class=Orders)


@router.patch("/orders/{order_id}")
def update_order(order_id: int, order_data: OrdersWrite, session: Session = Depends(get_session)):
    services.obj_update(session, order_id, order_data.model_dump(), obj_class=Orders)


@router.delete("/orders/{order_id}")
def delete_order(order_id: int, session: Session = Depends(get_session)):
    services.obj_delete(session, order_id, obj_class=Orders)
