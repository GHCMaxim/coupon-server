from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    SHOPPER = "shopper"
    EMPLOYEE = "employee"
    MANAGER = "manager"

class UserBase(BaseModel):
    username: str
    name: str
    email: str
    role: UserRole

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    pass


