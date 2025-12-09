from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from models import TaskStatus, TaskCategory

class TaskBase(BaseModel):
    title: str = Field(..., max_length=100, description="Task title")
    description: Optional[str] = Field(None, description="Task description")
    status: TaskStatus = Field(default=TaskStatus.pending, description="Task status")
    category: TaskCategory = Field(default=TaskCategory.other, description="Task category")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = Field(None, max_length=100)
    status: Optional[TaskStatus] = None
    category: Optional[TaskCategory] = None

class TaskStatusUpdate(BaseModel):
    status: TaskStatus

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True