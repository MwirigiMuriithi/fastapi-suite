# app/api/v1/task.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskInResponse
from app.services.task import TaskService

router = APIRouter()

# Dependency to get the database session
def get_task_service(db: Session = Depends(get_db)):
    return TaskService(db)

@router.post("/", response_model=TaskInResponse)
def create_task(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task)

@router.get("/", response_model=list[TaskInResponse])
def get_tasks(skip: int = 0, limit: int = 100, task_service: TaskService = Depends(get_task_service)):
    return task_service.get_tasks(skip=skip, limit=limit)

@router.get("/{task_id}", response_model=TaskInResponse)
def get_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    db_task = task_service.get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=TaskInResponse)
def update_task(task_id: int, task: TaskUpdate, task_service: TaskService = Depends(get_task_service)):
    db_task = task_service.update_task(task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", response_model=TaskInResponse)
def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    db_task = task_service.delete_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
