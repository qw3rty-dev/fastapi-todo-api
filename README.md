#  Todo API

A RESTful Todo API built with **FastAPI** and **SQLite** to practice backend fundamentals before moving to SQLAlchemy.

##  Features

- Create a task
- View all tasks
- View a task by ID
- Update a task (partial updates supported)
- Mark a task as completed
- Delete a task
- Delete all completed tasks
- Filter tasks by:
  - Task name
  - Priority
  - Due date
  - Completion status
  - Tasks with no due date
- Sort tasks by:
  - Task name
  - Priority (High → Medium → Low)
  - Due date
  - Completion status
- Request validation using Pydantic
- Proper HTTP status codes and error handling
- Dynamic SQL query building

---

##  Tech Stack

- Python 3
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

##  Project Structure

```
todo/
│
├── routes/
│   └── tasks.py
├── database.py
├── schemas.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    └── swagger.png
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/<qw3rty-dev>fastapi-todo-api.git
```

Go to the project directory:

```bash
cd todo-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

##  API Documentation

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

##  Preview

![Swagger UI](assets/swagger.png)

---

##  Learning Highlights

This project helped me practice:

- FastAPI routing
- CRUD operations
- Query parameters
- Path parameters
- Pydantic models
- Optional fields
- Enums
- Response models
- HTTP exceptions
- Dynamic SQL queries
- Filtering and sorting
- SQLite integration

---
