liczby2 = [1,2,3,4,5]
for liczba2 in liczby2:
    liczba2 = liczba2*2
    print(liczba2)

print("....................")

listaSkladana = [liczba2 * 2 for liczba2 in liczby2]
print(listaSkladana)
print("....................")