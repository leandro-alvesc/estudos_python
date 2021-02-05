# Escreva um prorgrama que leia 10 numeros e armazenar em um vetor, impriir o vetor, o maior e a posição do maior
vetor = []

for _ in range(10):
    vetor.append(int(input('Valor: ')))

print(vetor)
print(max(vetor))
print(vetor.index(max(vetor)))
