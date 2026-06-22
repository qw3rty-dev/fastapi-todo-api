from sqlalchemy.orm import Mapped,mapped_column
from datetime import date
from database import Base
from schemas import Priority

class Todo(Base):
    __tablename__ = "todo"
    task_id : Mapped[int] = mapped_column(primary_key= True)
    task_name : Mapped[str] = mapped_column(nullable= False,unique=True)
    priority : Mapped[Priority] = mapped_column(nullable= False)
    due_date : Mapped[date | None] = mapped_column(nullable=True)
    completed : Mapped[bool] = mapped_column(default= False)
