from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase, BaseModel):
    password: str


class UserOut(UserBase, BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

