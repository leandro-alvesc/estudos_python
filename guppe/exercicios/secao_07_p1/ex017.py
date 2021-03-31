# Ler um vetor de 10 posições e atribuir o valor 0 para os valores negativos
vetor = [int(input(f'Entre o valor {n+1}: ')) for n in range(10)]
novo_vetor = []

for item in vetor:
    if item < 0:
        item = 0
        novo_vetor.append(item)
    else:
        novo_vetor.append(item)

print(novo_vetor)
