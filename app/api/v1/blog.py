from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.blog import BlogCreate, Blog
from app.services.blog import create_new_blog, list_blogs, get_single_blog, edit_blog, remove_blog
from app.db.session import get_db
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Implement logic to verify the JWT token and get user
    return User(id=1)  # This is just a placeholder, implement token decoding and fetching user

@router.post("/", response_model=Blog)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_new_blog(db, blog, current_user.id)

@router.get("/", response_model=list[Blog])
def get_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return list_blogs(db, skip, limit)

@router.get("/{blog_id}", response_model=Blog)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return get_single_blog(db, blog_id)

@router.put("/{blog_id}", response_model=Blog)
def update_blog(blog_id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    return edit_blog(db, blog_id, blog)

@router.delete("/{blog_id}", response_model=Blog)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    return remove_blog(db, blog_id)
