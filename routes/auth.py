from fastapi import HTTPException,APIRouter,Query,Depends
from database import get_db
from schemas import UserCreate,MessageResponse,UserResponse,UserLogin,TokenResponse
from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import User
from utils.password import hash_password,verify_password
from datetime import UTC,datetime
from utils.jwt_handler import create_access_token,get_current_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/users",tags=["Users"])


@router.post("/register",response_model=UserResponse)
def register(user: UserCreate,
             db: Session= Depends(get_db)):
    existing_username = db.scalar(select(User).where(User.username == user.username))
    existing_email = db.scalar(select(User).where(User.email == user.email))

    if existing_username:
        raise HTTPException(status_code=400,detail= "Username already exists")
    if existing_email:
        raise HTTPException(status_code=400,detail= "Email already exists")
    
    new_user = User(username = user.username,
                    email = user.email,
                    hashed_password = hash_password(user.password))
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="User already exists")
    return new_user

@router.post("/login",response_model=TokenResponse)
def login(form_data:OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == form_data.username))
    if not user or not verify_password(form_data.password,user.hashed_password):
       raise HTTPException(status_code=401,detail="Invalid credentials")
    user.last_login = datetime.now(UTC)
    
    db.commit()
    token = create_access_token(user.id)
    return {"access_token": token,
            "token_type": "bearer"}

    
@router.get("/me",response_model= UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


    
    
    
    
