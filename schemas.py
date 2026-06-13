from pydantic import BaseModel
from datetime import date
from enum import Enum


class Priority(str,Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TodoCreate(BaseModel):
    task_name: str
    priority: Priority = Priority.low
    due_date: date | None = None
    completed: bool = False

class TodoResponse(BaseModel):
    task_id: int
    task_name: str
    priority: Priority = Priority.low
    due_date: date | None = None
    completed: bool = False
class TodoUpdate(BaseModel):

    task_name: str | None = None
    priority: Priority | None = None
    due_date: date | None = None
    completed: bool | None = None

    
class MessageResponse(BaseModel):
    message: str

class ShowResponse(BaseModel):
    total_tasks : int
    tasks : list[TodoResponse]
    

