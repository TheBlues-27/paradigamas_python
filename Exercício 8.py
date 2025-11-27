from collections import Counter
import math

def calcular_media(valores):
	return sum(valores) / len(valores)

def calcular_mediana(valores):
	ordenados = sorted(valores)
	n = len(ordenados)
	meio = n // 2
	if n % 2 == 1:
		return ordenados[meio]
	else:
		return (ordenados[meio - 1] + ordenados[meio]) / 2

def calcular_moda(valores):
	contagem = Counter(valores)
	if not contagem:
		return '—', 'Amodal'
	max_freq = max(contagem.values())
	if max_freq == 1:
		return '—', 'Amodal'
	modas = [v for v, freq in contagem.items() if freq == max_freq]
	if len(modas) == 1:
		return modas[0], 'Unimodal'
	elif len(modas) == 2:
		return modas, 'Bimodal'
	else:
		return modas, 'Multimodal'

def calcular_desvio_padrao(valores):
	media = calcular_media(valores)
	variancia = sum((x - media) ** 2 for x in valores) / len(valores)
	return math.sqrt(variancia)

print("Digite os valores separados por espaço:")
entrada = input().strip()
try:
	valores = [float(x.replace(',', '.')) for x in entrada.split()]
except ValueError:
	print("Entrada inválida. Certifique-se de digitar apenas números.")

if not valores:
	print("Nenhum valor informado.")


media = calcular_media(valores)
mediana = calcular_mediana(valores)
moda, tipo_moda = calcular_moda(valores)
desvio = calcular_desvio_padrao(valores)

print(f"\nValores: {valores}")
print(f"Média: {media:.3f}")
print(f"Mediana: {mediana:.3f}")
if tipo_moda == 'Amodal':
	print("Moda: — (Amodal)")
elif tipo_moda == 'Unimodal':
	print(f"Moda: {moda} (Unimodal)")
elif tipo_moda == 'Bimodal':
	print(f"Moda: {moda[0]} e {moda[1]} (Bimodal)")
else:
	print(f"Moda: {', '.join(str(m) for m in moda)} (Multimodal)")
print(f"Desvio padrão: {desvio:.3f}")

