from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "email": "example@gmail.com"
    #         }
    #     }


class UserCreate(UserBase):
    password: str
    class Config:
        schema_extra = {
            "example": {
                "email": "example@gmail.com",
                "password": "example"
            }
        }

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@gmail.com",
                "id": 0,
                "is_active": True,
                "items": []
            }
        }