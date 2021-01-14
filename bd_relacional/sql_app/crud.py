from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    new_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# def update_user(db: Session, user_id: int, user: schemas.UserCreate):
#     if user := get_user(db, user_id):
#         db.query(models.User).filter(
#             models.User.id == user_id
#         ).first().update(user)
#         db.commit()
#         db.refresh(user)

#         return user

# def update_user(db: Session, user_id: int, user: schemas.UserCreate):
#     return db.query(models.User).update().where(models.User.id == user_id).values(***user.dict())

# def update_user(db: Session, user_id: int, user: schemas.UserCreate):
#     return db.query(models.User).filter(models.User.id == user_id).\
#         update({
#             "email": "jpantunesdesouza13@gmail.com",
#             "id": 1,
#             "is_active": True,
#             "items": []
#         }, synchronize_session="fetch")

# def update_user(db: Session, user_id: int, user: schemas.UserCreate):
#     stmt = update(models.User).where(models.User.id == 1).values(
#         email = "testfunction@gmail.com"
#     ).\
#     execution_options(synchronize_session="fetch")

#     db.execute(stmt)
# 
