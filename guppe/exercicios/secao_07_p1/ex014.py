# Ler um vetor de 10 posições, verificar se há valores iguais e escreva na tela
vetor = []
iguais = []

for n in range(10):
    vetor.append(int(input(f'Posição {n}: ')))

for n in range(10):
    for c in range(10):
        if vetor[n] == vetor[c] and n != c and vetor[c] not in iguais:
            iguais.append(vetor[c])

print(vetor)
print(iguais)
