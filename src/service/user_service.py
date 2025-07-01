from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi import Depends, HTTPException, status
from typing import List

from src.models.user import User
from src.schema.user import UserCreate
from src.auth.jwt_handler import AuthHandler

auth_handler = AuthHandler()


def create_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered")

    hashed_password = auth_handler.get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password,role=user.role)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not auth_handler.verify_password(password, user.hashed_password):
        return False
    return user
