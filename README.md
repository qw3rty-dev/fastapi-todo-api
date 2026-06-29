# Todo API

A secure RESTful Todo API built with **FastAPI**, **SQLAlchemy 2.0**, and **SQLite**. The API supports user authentication using JWT, user-specific task management, filtering, sorting, partial updates, and follows RESTful design principles.

---

## Features

### Authentication

- User registration
- User login
- Password hashing using **pwdlib**
- JWT authentication
- Protected endpoints
- Retrieve current authenticated user (`/users/me`)

### Task Management

- Create new tasks
- Retrieve all tasks
- Retrieve a task by ID
- Update existing tasks
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

### Other Features

- User-specific task ownership
- Request & response validation using Pydantic
- SQLAlchemy 2.0 ORM
- Proper HTTP status codes and exception handling
- Interactive API documentation with Swagger UI

---

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy 2.0
- SQLite
- Pydantic v2
- Pwdlib
- PyJWT
- Uvicorn

---

## Project Structure

```text
todo/
├── assets/
│   └── swagger.png
├── routes/
│   ├── auth.py
│   └── tasks.py
├── utils/
│   ├── jwt_handler.py
│   └── security.py
├── database.py
├── models.py
├── schemas.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

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

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file from `.env.example`:

```env
SECRET_KEY=your_secret_key_here
```

Run the development server:

```bash
uvicorn main:app --reload
```

---

## Authentication

Most task endpoints require authentication.

1. Register a new account.
2. Login using your email and password.
3. Click **Authorize** in Swagger UI.
4. Enter your **email** in the **Username** field.
5. Enter your password.
6. Leave **Client ID** and **Client Secret** empty.
7. Click **Authorize**.

Swagger will automatically attach the JWT to all protected requests.

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users/register | Register a new user |
| POST | /users/login | Login and receive JWT |
| GET | /users/me | Retrieve current authenticated user |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tasks | Create a task |
| GET | /tasks | Retrieve all tasks |
| GET | /tasks/{task_id} | Retrieve a task by ID |
| PATCH | /tasks/edit/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |
| DELETE | /tasks/completed | Delete all completed tasks |

---

## API Documentation

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

---

## Preview

![Swagger UI](assets/Swagger.png)

---

## Example Queries

```http
GET /tasks?priority=high

GET /tasks?completed=true

GET /tasks?sort=priority&descending_order=true

GET /tasks?task_name=study

GET /tasks?show_null_due_date=true
```

---

## API Capabilities

- JWT Authentication
- Password Hashing
- User Authorization
- CRUD Operations
- Dynamic Filtering
- Dynamic Sorting
- Partial Updates (PATCH)
- SQLAlchemy 2.0 ORM
- SQLite Integration
- Pydantic Validation
- Response Validation
- Session Management
- RESTful API Design

---

## Future Improvements

- Refresh Tokens
- Email Verification
- Password Reset
- Pagination
- Docker Support
- PostgreSQL
- Alembic Migrations
- Automated Testing
- CI/CD Pipeline

---

