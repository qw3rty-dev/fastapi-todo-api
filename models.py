from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,UniqueConstraint
from datetime import date,datetime,UTC
from database import Base
from enums import Priority


class Todo(Base):
    __tablename__ = "todo"
    __table_args__ = (UniqueConstraint("user_id","task_name"),)

    id : Mapped[int] = mapped_column(primary_key= True)
    task_name : Mapped[str] = mapped_column(nullable= False)
    priority : Mapped[Priority] = mapped_column(nullable= False)
    due_date : Mapped[date | None] = mapped_column(nullable=True)
    completed : Mapped[bool] = mapped_column(default= False)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"),nullable= False)

    user: Mapped["User"] = relationship(back_populates= "todos")

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key= True)
    username: Mapped[str] = mapped_column(unique= True,nullable=False)
    email: Mapped[str] = mapped_column(unique= True,nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    
    is_active: Mapped[bool] = mapped_column(nullable=False,default=True)
    is_verified: Mapped[bool] = mapped_column(nullable=False,default=False)

    created_at: Mapped[datetime] = mapped_column(nullable=False,default= lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(nullable=False,default= lambda: datetime.now(UTC),onupdate= lambda: datetime.now(UTC))
    last_login: Mapped[datetime | None ] = mapped_column(nullable=True,default= None)
    
    todos: Mapped[list["Todo"]] = relationship(back_populates= "user")
    