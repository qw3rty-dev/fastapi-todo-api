from fastapi import FastAPI
from database import engine, Base
from routes import tasks
from routes import auth


Base.metadata.create_all(bind= engine)
app = FastAPI()
app.include_router(tasks.router)
app.include_router(auth.router)