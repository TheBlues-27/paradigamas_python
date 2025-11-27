gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

respostas = []

for i in range(10):
    resposta = input(f"Digite a resposta da questão {i + 1}: ").strip().upper()
    respostas.append(resposta)

pontuacao = 0
for i in range(10):
    if respostas[i] == gabarito[i]:
        pontuacao += 1
print(f"Sua pontuação final é: {pontuacao}/10")
print("Gabarito correto:")
for i in range(10):
    print(f"Questão {i + 1}: {gabarito[i]}")
    print(f"Sua resposta: {respostas[i]}")