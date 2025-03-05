from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
# from app.services.user import get_password_hash, verify_password, create_access_token
from app.services.user import (
    get_password_hash,
    verify_password,
    create_access_token,
    verify_token 
)
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.db.session import get_db
#from app.core.security import verify_token

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
