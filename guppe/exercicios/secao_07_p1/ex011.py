# Preencher um vetor com 10 numeros reais, calcule e mostre a quantidade de numeros negativos e a soma dos positivos
vetor = []
soma = 0
negativos = []

for n in range(10):
    valor = float(input(f'Entre o valor {n+1}: '))
    vetor.append(valor)
    if valor >= 0:
        soma += valor
    else:
        negativos.append(valor)

print(vetor)
print(f'A soma dos positivos: {soma}')
print(f'Negativos: {negativos}\nQuantidade de negativos: {len(negativos)}')
