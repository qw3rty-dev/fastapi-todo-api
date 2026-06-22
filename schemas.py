from pydantic import BaseModel,ConfigDict
from datetime import date
from enum import Enum


class Priority(str,Enum):
    low = "low"
    medium = "medium"
    high = "high"

class SortField(str,Enum):
    task_name = "task_name"
    priority = "priority"
    due_date = "due_date"
    completed = "completed"


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
    model_config = ConfigDict(from_attributes=True)

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
    

