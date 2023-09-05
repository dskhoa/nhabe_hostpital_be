from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String
from database.database import Base

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __allow_unmapped__ = True
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, default=None)
    password = Column(String, default=None)
    firstname: Column(String, default=None)
    lastname: Column(String, default=None)
    avatar: Column(String, default=None)
    role: Column(String, default=None)
    email: Column(String, default=None)
    phone: Column(String, default=None)
    identification: Column(String, default=None)
    created_at = Column(Integer, default=None)
    updated_at = Column(Integer, default=None)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)