def coDrugaLiczba(liczby3):

    if len(liczby3) != 10:
        raise ValueError("Lista musi zawierać dokładnie 10 liczb.")

    for i in range(1, len(liczby3), 2):
        print(liczby3[i])

inputLiczby = list(range(1, 11))
coDrugaLiczba(inputLiczby)