import sqlite3
import uuid

DB_NAME = 'queue.db'


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                status TEXT NOT NULL,
                payload TEXT
            )
        ''')
        conn.commit()


def produce_task():
    init_db()

    task_id = str(uuid.uuid4())
    status = 'pending'
    payload = f'Praca do wykonania {task_id[:8]}'

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (id, status, payload) VALUES (?, ?, ?)",
            (task_id, status, payload)
        )
        conn.commit()

    print(f"[Producer] Dodano zadanie do DB: {task_id} (status: pending)")


if __name__ == "__main__":
    produce_task()