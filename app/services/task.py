# app/services/task.py
from sqlalchemy.orm import Session
import app.db.task_crud as crud
from app.schemas.task import TaskCreate, TaskUpdate

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: TaskCreate):
        return crud.create_task(self.db, task)

    def get_tasks(self, skip: int = 0, limit: int = 100):
        return crud.get_tasks(self.db, skip, limit)

    def get_task(self, task_id: int):
        return crud.get_task(self.db, task_id)

    def update_task(self, task_id: int, task: TaskUpdate):
        return crud.update_task(self.db, task_id, task)

    def delete_task(self, task_id: int):
        return crud.delete_task(self.db, task_id)
