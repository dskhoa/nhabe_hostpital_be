from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional
from entities.auth import User as UserEntity
from models.user import User, UserUpdateRequest

class UserRepository:
    @staticmethod
    def get_user(db: Session, user_id: int) -> Optional[UserEntity]:
        return db.query(UserEntity).filter(UserEntity.id == user_id).first()

    @staticmethod
    def get_user_by_name(db: Session, username: str) -> Optional[UserEntity]:
        return db.query(UserEntity).filter(UserEntity.username == username).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[UserEntity]:
        return db.query(UserEntity).offset(skip).limit(limit).all()

    @staticmethod
    def update_user(db: Session, user_id: int, user: UserUpdateRequest) -> UserEntity:
        db_user = UserRepository.get_user(db, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        update_data = user.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.now()
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int) -> None:
        db_user = UserRepository.get_user(db, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(db_user)
        db.commit()
