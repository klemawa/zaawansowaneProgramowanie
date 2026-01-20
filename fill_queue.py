import producer
import time

start = time.time()

print("Generuję 100 zadań do bazy SQLite...")
for i in range(100):
    producer.produce_task()

print(f"Gotowe. Czas operacji: {time.time() - start:.2f}s")