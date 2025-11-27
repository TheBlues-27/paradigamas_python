
n = int(input("Digite um número inteiro positivo: "))
steps = 0
sequence = [n]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    sequence.append(n)
    steps += 1

print(" -> ".join(map(str, sequence)))
print(f"Passos: {steps}")
