import csv
import time


def read_tasks(file_path='tasks.csv'):
    tasks = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            tasks.append(row)
    return tasks


def update_tasks(tasks, file_path='tasks.csv'):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow(task)


def consume_task(file_path='tasks.csv'):
    while True:
        tasks = read_tasks(file_path)
        for task in tasks:
            if task[1] == 'pending':  # Szukamy pierwszej pracy w statusie "pending"
                print(f"Processing task with ID: {task[0]}")
                task[1] = 'in_progress'
                update_tasks(tasks, file_path)

                # Symulowanie wykonywania pracy
                time.sleep(30)

                # Zmiana statusu na "done"
                task[1] = 'done'
                update_tasks(tasks, file_path)
                print(f"Task with ID: {task[0]} completed")
                break

        # Oczekiwanie 5 sekund przed ponownym sprawdzeniem
        time.sleep(5)


if __name__ == "__main__":
    consume_task()
