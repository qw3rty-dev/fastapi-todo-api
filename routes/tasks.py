from fastapi import HTTPException,APIRouter,Query,Depends
from database import get_db
from schemas import TodoResponse,TodoCreate,MessageResponse,ShowResponse,TodoUpdate
from enums import SortField,Priority
from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select,case
from models import Todo,User
from utils.jwt_handler import get_current_user
router = APIRouter(prefix= "/tasks",tags=["tasks"])


@router.post("/",response_model=MessageResponse)
def create_task(todo:TodoCreate,
                current_user: User = Depends(get_current_user),
                db: Session = Depends(get_db)):
    new_todo = Todo(task_name= todo.task_name,
                    priority= todo.priority,
                    due_date= todo.due_date,
                    completed= todo.completed,
                    user_id= current_user.id)
    try:
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="Task already exists")
    return {"message":"task added"}



@router.get("/",response_model=ShowResponse)
def show_task(
    task_name:str | None = Query(default=None),
    completed:bool | None = Query(default=None),
    priority:Priority | None = Query(default=None),
    due_date:date | None = Query(default=None),
    sort:SortField | None = Query(default = None),
    descending_order: bool = Query(False,description="Sort in descending order"),
    show_null_due_date:bool | None = Query(default=None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
 
    query = select(Todo).where(Todo.user_id == current_user.id)
    if task_name:
        query = query.where(Todo.task_name.ilike(f"%{task_name}%"))
    if completed is not None:
        query = query.where(Todo.completed == completed)
    if priority:
        query = query.where(Todo.priority == priority)
    if due_date is not None:
        query = query.where(Todo.due_date == due_date)
    if show_null_due_date:
        query = query.where(Todo.due_date.is_(None))
    if sort:                        

        if sort == "priority":
            sort_expression = case(
                (Todo.priority == Priority.high,1),
                (Todo.priority == Priority.medium,2),
                (Todo.priority == Priority.low,3)
            )
        else:
            sort_expression = getattr(Todo,sort.value)
        
        order = sort_expression.desc() if descending_order else sort_expression.asc()
        
        query = query.order_by(order)
    todos = db.scalars(query).all()
    return {"total_tasks": len(todos),
             "tasks": todos}



@router.patch("/edit/{task_id}",response_model=MessageResponse)
def edit_task(update:TodoUpdate,task_id:int,
              current_user: User = Depends(get_current_user),
              db: Session= Depends(get_db)):

    task = db.scalar(select(Todo).where(Todo.id==task_id,Todo.user_id == current_user.id))
    if task is None:
        raise HTTPException(status_code=404,detail = "Task not found")   
    data = update.model_dump(exclude_unset= True)
    if not data:
        return {"message": "No changes detected"}

    for field, value in data.items():
        setattr(task,field,value)
    
    if not db.is_modified(task):
        return {"message": "No changes detected"}
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="Task already exists")
    return {"message": "Task Updated"}
   


@router.delete("/completed",response_model=MessageResponse)
def delete_completed_tasks(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    completed_tasks = db.scalars(select(Todo).where(Todo.user_id == current_user.id,Todo.completed.is_(True))).all()
    if not completed_tasks:
        return {"message": "No completed tasks found"}
    
    for task in completed_tasks:
        db.delete(task)
        
    db.commit()
    return {"message": f"{len(completed_tasks)} Task(s) deleted"}

    
     
@router.delete("/{task_id}",response_model=MessageResponse)
def delete_task(task_id: int,
                current_user: User = Depends(get_current_user),
                db: Session = Depends(get_db)):
    task = db.scalar(select(Todo).where(Todo.id==task_id,Todo.user_id == current_user.id))
    if task is None:
        raise HTTPException(status_code=404,detail = "Task not found")   
    db.delete(task)  
    db.commit()
    return {"message": "Task deleted"}



@router.get("/{task_id}",response_model=TodoResponse)
def show_task_by_id(task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):

    query = select(Todo).where(Todo.user_id == current_user.id,Todo.id == task_id)
    task = db.scalar(query)
    if task is None:
       raise HTTPException(status_code=404,detail = "Task not found")

    return task
