import random

n = int(input("Digite o número (inteiro positivo) de lançamentos: "))

if n <= 0:
    print("O número de lançamentos deve ser maior que zero.")
else:
    contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(n):
        face = random.randint(1, 6)
        contadores[face] += 1

    print("\n" + "="*50)
    for face in range(1, 7):
        vezes = contadores[face]
        percentual = (vezes / n) * 100
        print(f"Face {face}: {vezes:,d} vezes ({percentual:.2f}%)")
    print("="*50)