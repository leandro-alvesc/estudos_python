# Ler a nota da prova de 15 alunos e armazenar num vetor, imprimir a média geral
vetor = []

for n in range(15):
    vetor.append(float(input(f'Entre o valor do aluno {n+1}: ')))

media = sum(vetor) / len(vetor)

print(f'Média: {media:.2f}')
