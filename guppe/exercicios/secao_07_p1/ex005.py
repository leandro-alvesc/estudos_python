# Ler um vetor de 10 posições. Contar e escrever quantos valores pares ele possui
vetor = []
for _ in range(10):
    vetor.append(int(input('Digite o valor: ')))

pares = [n for n in vetor if n % 2 == 0]

print(f'Pares: {pares}')
print(f'Quantidade de pares: {len(pares)}')
