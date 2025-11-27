def main():
	while True:
		try:
			n = int(input("Digite um número inteiro positivo (n): "))
			if n <= 0:
				print("Por favor, um inteiro positivo maior que zero.")
				continue
			break
		except ValueError:
			print("Entrada inválida — digite um número inteiro.")

	for k in range(1, n + 1):
		t = k * (k + 1) // 2
		print(f"T{k} = {t}")


if __name__ == "__main__":
	main()

