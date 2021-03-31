# Escreva um programa que leia numeros inteiros no intervalo [0, 50] e os armazene em um vetor com 10 posicoese preencha
# um segundo vetor apenas com os numeros impares do primeiro vetor, imprima os dois vetores 2 elementos por linha
vetor = []
n = 1
while n <= 10:
    valor = int(input(f'Entre o valor {n}: '))
    if 0 < valor > 50:
        print('Valor inválido')
    else:
        vetor.append(valor)
        n += 1

novo_vetor = [item for item in vetor if item % 2 != 0]

for i in range(0, len(vetor), 2):
    print(f'{vetor[i]} {vetor[i+1]}')

print()

for i in range(0, len(novo_vetor), 2):
    if len(novo_vetor) % 2 != 0:
        novo_vetor.append('-')
    print(f'{novo_vetor[i]} {novo_vetor[i+1]}')
