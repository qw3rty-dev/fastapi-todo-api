from fastapi import HTTPException,APIRouter,Query
from database import get_connection
from schemas import TodoResponse,TodoCreate,MessageResponse,ShowResponse,Priority,TodoUpdate
from datetime import date
from sqlite3 import IntegrityError
router = APIRouter(prefix= "/tasks",tags=["tasks"])


@router.post("/",response_model=MessageResponse)
def create_task(todo:TodoCreate):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO todo (task_name,priority,due_date,completed) values (?,?,?,?)",(todo.task_name,todo.priority,todo.due_date,todo.completed))
        conn.commit()
    except IntegrityError:
        raise HTTPException(status_code=409,detail="Task already exists")
    conn.close()
    return {"message":"task added"}

@router.get("/",response_model=ShowResponse)
def show_task(
    task_name:str | None = Query(default=None),
    completed:bool | None = Query(default=None),
    priority:Priority | None = Query(default=None),
    due_date:date | None = Query(default=None),
    sort:str | None = Query(default = None),
    show_null_due_date:bool | None = Query(default=None)):
     conn = get_connection()
     cursor = conn.cursor()
     query = "SELECT * FROM todo "
     conditions = []
     params= []
     if task_name:
         conditions.append("task_name LIKE ?")
         params.append(f"%{task_name}%")
     if completed is not None:
         conditions.append("completed = ?")
         params.append(int(completed))
     if priority:
         conditions.append("priority = ?")
         params.append(priority)
     if due_date is not None:
         conditions.append("due_date = ?")
         params.append(due_date)
     if show_null_due_date:
         conditions.append("due_date IS NULL")  

     if conditions:
         query += " WHERE " + " AND ".join(conditions)
     if sort:
         conditions = []
         if sort == "due_date":
          conditions.append("ORDER BY due_date IS NULL,due_date")

         elif sort == "priority":
            conditions.append("""ORDER BY CASE priority
                            WHEN 'high' THEN 1
                            WHEN 'medium' THEN 2
                            WHEN 'low' THEN 3
                            END """)
         elif sort == "task_name":
            conditions.append("ORDER BY task_name COLLATE NOCASE")

         elif sort == "completed":
            conditions.append("ORDER BY completed DESC")
         else:
            raise HTTPException(status_code=400,detail= f"Invalid metric.Choose from (task_name,priority,due_date,completed)")
         if conditions:
              query += conditions[0]
         
     cursor.execute(query,params)
     rows = cursor.fetchall()
     conn.close()
     return {"total_tasks": len(rows),
             "tasks": [dict(row) for row in rows]}

@router.get("/{task_id}",response_model=TodoResponse)
def show_task_by_id(task_id: int):
     
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM todo where task_id = ?",(task_id,))
     row = cursor.fetchone()
     if row:
        conn.close()
        return dict(row)
     raise HTTPException(status_code=404,detail= "Task not found")

@router.patch("/edit/{tasks_id}",response_model=MessageResponse)
def edit_task(todo:TodoUpdate,task_id:int):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM todo WHERE task_id = ?", (task_id,))
     
     task =cursor.fetchone()
     if task is None:
         conn.close()
         raise HTTPException(status_code=404,detail = "Task not found")   
     
     query = "UPDATE todo SET "
     params = []
     toedit = []
     if todo.task_name is not None and todo.task_name != task['task_name']:
         toedit.append("task_name = ?")
         params.append(todo.task_name)
     if todo.priority and todo.priority != task['priority']:
         toedit.append("priority = ?")
         params.append(todo.priority)
     if todo.due_date and todo.due_date != task['due_date']:
         toedit.append("due_date = ?")
         params.append(todo.due_date)
     if todo.completed is not None and todo.completed != task['completed']:
         toedit.append("completed = ?")
         params.append(todo.completed)
     if toedit:
         query += ", ".join(toedit) + " WHERE task_id = ? "
         params.append(task_id)
        
         print(query)
         cursor.execute(query,params)
         conn.commit()
         conn.close()
         return {"message": "Task Updated"}
     conn.close()
     return{"message": "No changes detected"}


@router.patch("/{task_id}",response_model=MessageResponse)
def mark_completed(task_id: int):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute("UPDATE todo set completed = 1 where task_id = ?",(task_id,))
     conn.commit()
     if cursor.rowcount>0:
         conn.close()
         return {"message": "Task marked as completed"}
     raise HTTPException(status_code=404,detail= "Task not found")

@router.delete("/{task_id}",response_model=MessageResponse)
def remove_task(task_id: int):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute("DELETE FROM todo where task_id = ?",(task_id,))
     conn.commit()
     conn.close()
     return {"message": "Task removed"}
     

@router.delete("/completed",response_model=MessageResponse)
def remove_completed():
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute("DELETE FROM todo where completed = 1")
     conn.commit()
     conn.close()
     return {"message": f"{cursor.rowcount} completed task(s) removed"}
     

# @router.get("/sort")
# def sort_tasks(metric: str):
#      conn = get_connection()
#      cursor = conn.cursor()
#      query = "SELECT * FROM todo "
#      if metric == "due_date":
#          query += "ORDER BY due_date IS NULL,due_date "

#      elif metric == "priority":
#          query += """ORDER BY CASE priority
#                          WHEN 'high' THEN 1
#                          WHEN 'medium' THEN 2
#                          WHEN 'low' THEN 3
#                          END """
#      elif metric == "task_name":
#           query += "ORDER BY task_name COLLATE NOCASE "

#      elif metric == "completed":
#           query += "ORDER BY completed DESC "
#      else:
#          raise HTTPException(status_code=400,detail= f"Invalid metric.Choose from (task_name,priority,due_date,completed)")
         
#      cursor.execute(query)
#      rows = cursor.fetchall()
#      conn.close()
#      return [dict(row) for row in rows]
