# Ler um conjunto de numeros reais (10) e armazenar em um vetor e calcular o quadrado dos componentes colocando-o em
# outro vetor, imprimir todos os conjuntos
v1 = []
v2 = []
for n in range(10):
    v1.append(float(input('Entre um valor real: ')))
    v2.append(v1[n] ** 2)

print(v1)
print(v2)
