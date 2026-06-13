import sqlite3



def get_connection():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS todo (
                   task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   task_name TEXT UNIQUE,
                   priority TEXT DEFAULT 'low' 
                        CHECK (priority IN ('low','medium','high')),
                   due_date DATE,
                   completed BOOLEAN);
                   """)
    conn.commit()
    conn.close()