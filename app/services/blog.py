from sqlalchemy.orm import Session
from app.db.blog_crud import create_blog, get_blogs, get_blog, update_blog, delete_blog
from app.schemas.blog import BlogCreate
from fastapi import HTTPException, status

def create_new_blog(db: Session, blog: BlogCreate, user_id: int):
    return create_blog(db, blog, user_id)

def list_blogs(db: Session, skip: int, limit: int):
    return get_blogs(db, skip, limit)

def get_single_blog(db: Session, blog_id: int):
    blog = get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog

def edit_blog(db: Session, blog_id: int, blog: BlogCreate):
    existing_blog = get_blog(db, blog_id)
    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return update_blog(db, blog_id, blog)

def remove_blog(db: Session, blog_id: int):
    existing_blog = get_blog(db, blog_id)
    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return delete_blog(db, blog_id)
