import math

numero = int(input("Digite um número inteiro positivo maior que 20: "))

if numero <= 20:
    print("Número inválido! O número deve ser maior que 20.")
else:
    fator = math.factorial(numero)
    print(f"{numero}!=23{fator}")