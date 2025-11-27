def format_num_ptbr(value, decimals=3):
    fmt = f"{value:.{decimals}f}"
    return fmt.replace('.', ',')

nome = input("Atleta: ")

saltos = []
labels = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
for i, lbl in enumerate(labels, start=1):
    while True:
        try:
            val = float(input(f"{lbl} Salto: ").strip())
            saltos.append(val)
            break
        except ValueError:
            print("Entrada inválida. Informe um número (ex.: 6.1)")

melhor = max(saltos)
pior = min(saltos)

restantes = saltos.copy()
restantes.remove(melhor)
restantes.remove(pior)

media = sum(restantes) / len(restantes)

print()
print(f"Atleta: {nome}")
print("---------------------------------")
for i, val in enumerate(saltos, start=1):
    print(f"{labels[i-1]} Salto: {val:.1f} m")
print("---------------------------------")
print(f"Melhor salto: {melhor:.1f} m")
print(f"Pior salto : {pior:.1f} m")

a, b, c = restantes
mediastr = format_num_ptbr(media, 3)
print(f"Média considerada = ( {a:.1f} + {b:.1f} + {c:.1f} ) / 3 = {mediastr} m")