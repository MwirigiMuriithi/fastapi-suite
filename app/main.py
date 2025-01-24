from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1 import task
from app.api.v1 import note

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])
app.include_router(note.router, prefix="/notes", tags=["notes"])



@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}

