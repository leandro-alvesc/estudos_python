# Ler 5 valores e mostrar todos os lidos, com o maior, o menor e a média
vetor = []

for n in range(5):
    vetor.append(int(input(f'Valor {n+1}: ')))

print(vetor)
print(max(vetor))
print(min(vetor))
print(sum(vetor) / len(vetor))
