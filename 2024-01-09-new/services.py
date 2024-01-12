from sqlalchemy import insert, update, delete
from sqlalchemy.orm import Session


def obj_create(session: Session, obj_data: dict, obj_class):
    stmt = insert(obj_class).values(**obj_data)
    session.execute(stmt)
    session.commit()


def obj_get(session: Session, offset: int, limit: int, obj_class):
    return session.query(obj_class).offset(offset).limit(limit).all()


def obj_get_by_id(session: Session, obj_id: int, obj_class):
    return session.query(obj_class).filter(obj_class.id == obj_id).first()


def obj_get_by_email(session: Session, obj_email: str, obj_class):
    return session.query(obj_class).filter(obj_class.email == obj_email).first()


def obj_update(session: Session, obj_id, obj_data: dict, obj_class):
    stmt = update(obj_class).values(**obj_data).where(obj_class.id == obj_id)
    session.execute(stmt)
    session.commit()


def obj_delete(session: Session, obj_id: int, obj_class):
    stmt = delete(obj_class).where(obj_class.id == obj_id)
    session.execute(stmt)
    session.commit()
