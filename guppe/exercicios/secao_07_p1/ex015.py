# Ler um vetor com 20 numeros. Eliminar os repetidos
vetor = []
unicos = []
for n in range(5):
    vetor.append(int(input(f'Posição {n}: ')))

for n in range(5):
    for c in range(5):
        if vetor[n] != vetor[c] and n != c and vetor[c] not in unicos:
            unicos.append(vetor[c])

vetor = unicos.copy()
print(vetor)
