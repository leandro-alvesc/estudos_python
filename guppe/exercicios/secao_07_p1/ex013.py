# Ler 5 valores e em seguida mostrar a posição onde se encontram o maior e o menor
vetor = []

for n in range(5):
    vetor.append(int(input(f'Valor {n+1}: ')))

print(vetor.index(max(vetor)))
print(vetor.index(min(vetor)))
