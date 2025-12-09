from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
from database import Base
import enum

class TaskStatus(str, enum.Enum):
    pending = "pending"
    completed = "completed"

class TaskCategory(str, enum.Enum):
    work = "work"
    personal = "personal"
    study = "study"
    other = "other"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    category = Column(Enum(TaskCategory), default=TaskCategory.other)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)