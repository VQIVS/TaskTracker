from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repository.task_repository import get_tasks, get_task, create_task, update_task, delete_task
from schemas.task import TaskCreate, TaskUpdate, TaskResponse
from models.task import Task
from database import get_db

router = APIRouter()

@router.get("/tasks", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.post("/tasks", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.dict())
    return create_task(db, new_task)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task(db, task_id, task.dict())
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
