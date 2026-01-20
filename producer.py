import csv
import uuid
import os

FILE_NAME = 'tasks.csv'


def produce_task():
    # Sprawdź czy plik istnieje, jeśli nie - stwórz nagłówki
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'status', 'payload']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        # Generujemy unikalne ID dla zadania
        task_id = str(uuid.uuid4())

        # Zapisujemy 1 rekord ze statusem 'pending'
        writer.writerow({
            'id': task_id,
            'status': 'pending',
            'payload': f'Praca do wykonania {task_id[:8]}'
        })

        print(f"[Producer] Dodano zadanie: {task_id} (status: pending)")


if __name__ == "__main__":
    produce_task()