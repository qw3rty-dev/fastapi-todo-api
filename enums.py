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
