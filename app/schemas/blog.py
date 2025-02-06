from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: str  # You can change this to a datetime object if needed.

    class Config:
        orm_mode = True
