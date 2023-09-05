from typing import Optional

from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    id: Optional[int]
    username: Optional[str]
    password: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    avatar: Optional[str]
    role: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    identification: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)


class UserUpdateRequest(BaseModel):
    username: Optional[str]
    password: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    avatar: Optional[str]
    role: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    identification: Optional[str]
