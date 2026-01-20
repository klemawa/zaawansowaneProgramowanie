import producer

print("Rozpoczynam dodawanie 100 zadań...")
for i in range(100):
    producer.produce_task()
print("Zakończono dodawanie 100 zadań.")