# Ler uma matriz 4x4 contar e escrever quantos valores maiores que 10 ela possui
vetor = [[int(input(f'Valor {n}: ')) for n in range(4)] for valor in range(4)]
maior_q_10 = []
for n in vetor:
    for c in range(4):
        if n[c] > 10:
            maior_q_10.append(n[c])

print(maior_q_10)
print(f'Quantidade de valores maiores que 10: {len(maior_q_10)}')
