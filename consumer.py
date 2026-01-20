import csv
import time
import os
import shutil
from tempfile import NamedTemporaryFile

FILE_NAME = 'tasks.csv'
WORK_DURATION = 30  # czas trwania pracy w sekundach
POLL_INTERVAL = 5  # co ile sprawdzać plik


def update_task_status(target_task_id, new_status):
    """
    Funkcja pomocnicza do bezpiecznej aktualizacji statusu w pliku CSV.
    Tworzy plik tymczasowy, przepisuje dane ze zmianą i podmienia pliki.
    """
    temp_file = NamedTemporaryFile(mode='w', newline='', delete=False, encoding='utf-8')
    updated = False

    with open(FILE_NAME, 'r', encoding='utf-8') as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row['id'] == target_task_id:
                row['status'] = new_status
                updated = True
            writer.writerow(row)

    shutil.move(temp_file.name, FILE_NAME)
    return updated


def get_pending_task():
    """Zwraca ID pierwszego zadania o statusie pending"""
    if not os.path.isfile(FILE_NAME):
        return None

    with open(FILE_NAME, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['status'] == 'pending':
                return row['id']
    return None


def run_consumer():
    print("[Consumer] Start. Oczekiwanie na zadania...")

    while True:
        task_id = get_pending_task()

        if task_id:
            # 1. Zmiana statusu na in_progress
            print(f"[Consumer] Pobrano zadanie: {task_id}. Zmieniam na 'in_progress'...")
            update_task_status(task_id, 'in_progress')

            # 2. Symulacja pracy (30s)
            print(f"[Consumer] Wykonuję pracę dla {task_id} (trwa {WORK_DURATION}s)...")
            time.sleep(WORK_DURATION)

            # 3. Zmiana statusu na done
            print(f"[Consumer] Zakończono pracę nad {task_id}. Zmieniam na 'done'.")
            update_task_status(task_id, 'done')

        else:
            # Brak zadań - czekaj 5 sekund
            print(f"[Consumer] Brak zadań 'pending'. Sprawdzę za {POLL_INTERVAL}s.")
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    run_consumer()