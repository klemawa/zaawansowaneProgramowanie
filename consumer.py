import sqlite3
import time

DB_NAME = 'queue.db'
WORK_DURATION = 30
POLL_INTERVAL = 5


def claim_task():
    task_id = None

    # Używamy context managera, który automatycznie obsługuje transakcje
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        #Znajdź jedno zadanie pending
        cursor.execute("SELECT id FROM tasks WHERE status='pending' LIMIT 1")
        row = cursor.fetchone()

        if row:
            task_id = row[0]
            #Od razu oznacz jako in_progress (blokujemy dla innych)
            cursor.execute("UPDATE tasks SET status='in_progress' WHERE id=?", (task_id,))
            conn.commit()
            return task_id
        else:
            return None


def mark_task_done(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status='done' WHERE id=?", (task_id,))
        conn.commit()


def run_consumer():
    print("[Consumer SQL] Start. Oczekiwanie na zadania w bazie...")

    #Dla bezpieczeństwa:
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("SELECT count(*) FROM tasks")
    except sqlite3.OperationalError:
        print("[Consumer] Tabela nie istnieje. Uruchom najpierw Producera.")
        return

    while True:
        #Pobranie i zmiana statusu na in_progress
        task_id = claim_task()

        if task_id:
            print(f"[Consumer] Pobrano zadanie: {task_id}. Status: 'in_progress'.")

            #Symulacja pracy
            print(f"[Consumer] Wykonuję pracę... ({WORK_DURATION}s)")
            time.sleep(WORK_DURATION)

            #Zmiana statusu na done
            mark_task_done(task_id)
            print(f"[Consumer] Zakończono {task_id}. Status: 'done'.")

        else:
            print(f"[Consumer] Brak zadań 'pending'. Czekam {POLL_INTERVAL}s...")
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    run_consumer()