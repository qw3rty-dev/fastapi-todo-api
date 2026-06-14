#  Todo API

A RESTful Todo API built with **FastAPI** and **SQLite** for efficient task management. The API allows users to create, update, search, filter, sort, and manage tasks through clean and well-structured REST endpoints.

---

##  Features

- Create new tasks
- Retrieve all tasks
- Retrieve a task by ID
- Update existing tasks
- Mark tasks as completed
- Delete individual tasks
- Delete all completed tasks
- Search tasks by name
- Filter tasks by:
  - Priority
  - Completion status
  - Due date
  - Tasks without a due date
- Sort tasks by:
  - Task name
  - Priority
  - Due date
  - Completion status
- Request validation using Pydantic
- Proper HTTP status codes and exception handling
- Interactive API documentation with Swagger UI

---

##  Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

##  Project Structure

```text
todo/
├── assets/
│   └── swagger.png
├── routes/
│   └── tasks.py
├── database.py
├── schemas.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/qw3rty-dev/fastapi-todo-api.git
```

Navigate to the project directory:

```bash
cd fastapi-todo-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn main:app --reload
```

---

##  API Documentation

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

---

##  Preview

![Swagger UI](assets/swagger.png)

---

##  API Capabilities

- CRUD operations
- Dynamic filtering using query parameters
- Dynamic sorting
- Partial updates (PATCH)
- Pydantic request & response models
- Enum-based priority validation
- Parameterized SQL queries
- SQLite database integration

---

##  Future Improvements

- SQLAlchemy ORM integration
- JWT Authentication
- User authentication & authorization
- Pagination
- Docker support
- Automated testing
- PostgreSQL support

---
