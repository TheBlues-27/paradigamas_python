a, b = 0, 1
sequencia = []

while a <= 500:
    sequencia.append(a)
    a, b = b, a + b

sequencia.append(a)

print("Números de Fibonacci:\n")
for i, num in enumerate(sequencia):
    marcador = " ← ULTRAPASSA 500!" if num > 500 else ""
    print(f"F({i}) = {num}{marcador}")

print(f"\nTotal de números gerados: {len(sequencia)}")
print(f"Último valor: {sequencia[-1]}")