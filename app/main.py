from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1 import task
from app.api.v1 import note
from app.api.v1 import chat
from app.api.v1 import blog


app = FastAPI()


app.include_router(blog.router, prefix="/blogs", tags=["blogs"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])
app.include_router(note.router, prefix="/notes", tags=["notes"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])




@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}

