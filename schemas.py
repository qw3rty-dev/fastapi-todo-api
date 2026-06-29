from pydantic import BaseModel,ConfigDict,EmailStr,Field
from datetime import date,datetime
from enums import Priority

class TodoCreate(BaseModel):
    task_name: str
    priority: Priority = Priority.low
    due_date: date | None = None
    completed: bool = False

class TodoResponse(BaseModel):
    id: int
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
    

# _______________________________user__________________________________


class UserCreate(BaseModel):
    username: str = Field(min_length=3,max_length=30)
    email: EmailStr
    password: str = Field(min_length=8,max_length=128)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_verified: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

    
class UserLogin(BaseModel):
    email: EmailStr
    password: str= Field(min_length=8,max_length=128)


#________________________________TokenResponse__________________________

class TokenResponse(BaseModel):
    access_token: str
    token_type: str


