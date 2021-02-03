# Ler um vetor de 8 posicoes e em seguida ler dois valores x e y correspondentes a posição do vetor. Somar dois valores
# nas respectivas posicoes
vetor = []
for _ in range(8):
    vetor.append(int(input('Insira um número ao vetor: ')))

x = int(input('Número de 0 a 7: '))
y = int(input('Número de 0 a 7: '))

print(f'A soma do vetor na posição {x} e do vetor na posição {y} é: {vetor[x] + vetor[y]}')
