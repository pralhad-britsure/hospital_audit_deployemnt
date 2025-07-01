from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schema.user import UserCreate,UserResponse,UserLogin,Token
from src.service.user_service import create_user, authenticate_user
from src.database import get_db
from src.auth.jwt_handler import AuthHandler
from src.models.user import User

router = APIRouter(tags=["Authentication"])
auth_handler = AuthHandler()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_credentials.email, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_handler.encode_token(user.id, user.role)
    return {"access_token": access_token, "token_type": "bearer", "role": user.role}

@router.get("/me", response_model=UserResponse)
def get_current_user(auth_data=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    user_id = auth_data["user_id"]
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

