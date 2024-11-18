import csv
from datetime import datetime


def add_task(file_path='tasks.csv'):
    # Tworzenie nowego rekordu z pracą
    task_id = datetime.now().strftime('%Y%m%d%H%M%S')
    task = [task_id, 'pending']  # ID pracy i status początkowy

    # Zapisywanie do pliku
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(task)
        print(f"Added new task with ID: {task_id}")


if __name__ == "__main__":
    add_task()
