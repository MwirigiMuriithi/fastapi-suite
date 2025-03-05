# from fastapi import FastAPI
# from app.api.v1.auth import router as auth_router
# from app.api.v1 import task
# from app.api.v1 import note
# from app.api.v1 import chat
# from app.api.v1 import blog

# app = FastAPI()

# app.include_router(blog.router, prefix="/blogs", tags=["blogs"])
# app.include_router(auth_router, prefix="/auth", tags=["auth"])
# app.include_router(task.router, prefix="/tasks", tags=["tasks"])
# app.include_router(note.router, prefix="/notes", tags=["notes"])
# app.include_router(chat.router, prefix="/chat", tags=["chat"])

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Task Manager API"}

from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.task import router as task_router
from app.api.v1.note import router as note_router
from app.api.v1.chat import router as chat_router
from app.api.v1.blog import router as blog_router
import app.models.user  
import app.models.blog  
import app.models.chat  
import app.models.note  
import app.models.task  

from app.db.session import engine, Base

# Create database tables if they don't exist (development only)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog_router, prefix="/blogs", tags=["blogs"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(note_router, prefix="/notes", tags=["notes"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}
