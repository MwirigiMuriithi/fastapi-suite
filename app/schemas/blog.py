from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: str 

    class Config:
        orm_mode = True


