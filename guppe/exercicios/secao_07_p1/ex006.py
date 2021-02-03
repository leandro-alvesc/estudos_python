# Receba um vetor com 10 posições, retornar o maior e menor elemento do vetor
vetor = []
for _ in range(10):
    vetor.append(int(input('Digite o valor: ')))

print(f'Maior: {max(vetor)}')
print(f'Menor: {min(vetor)}')
