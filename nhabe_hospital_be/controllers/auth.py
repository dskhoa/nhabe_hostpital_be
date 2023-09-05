import os

from fastapi import APIRouter, Depends, HTTPException
from jose import JWTError, jwt
from models.user import User, UserUpdateRequest
from services import auth as auth_service
from fastapi import status
from repositories.user import UserRepository
from sqlalchemy.orm import Session

from database.database import SessionLocal

router = APIRouter()
SECRET_KEY = os.getenv('SECRET_KEY', 'nhabehospital')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/token")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(username, password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth_service.create_access_token(data={"sub": user.username})
    refresh_token = auth_service.create_refresh_token(data={"sub": user.username})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.post("/refresh-token")
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = UserRepository.get_user_by_name(db, username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.get_current_user(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
