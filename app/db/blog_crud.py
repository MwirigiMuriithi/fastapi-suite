from sqlalchemy.orm import Session
from app.models.blog import Blog
from app.schemas.blog import BlogCreate

def create_blog(db: Session, blog: BlogCreate, user_id: int):
    db_blog = Blog(**blog.dict(), user_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Blog).offset(skip).limit(limit).all()

def get_blog(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()

def update_blog(db: Session, blog_id: int, blog: BlogCreate):
    db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if db_blog:
        db_blog.title = blog.title
        db_blog.content = blog.content
        db.commit()
        db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog
