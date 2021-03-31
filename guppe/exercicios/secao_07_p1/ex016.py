"""
# Ler um vetor de 5 posições para numeros reais depois um codigo inteiro.
0 - finalize o programa
1 - mostre o vetor na ordem direta
2 - mostre o vetor na ordem inversa
"""
print('Entre os valores do vetor: ')

vetor = [float(input(f'Valor {n}: ')) for n in range(5)]

print(
    """Escolha uma opção abaixo:
0 - Finalize o programa
1 - Mostre o vetor na ordem direta
2 - Mostre o vetor na ordem inversa
    """
)

codigo = int(input('Digite a opção desejada: '))

if codigo == 0:
    exit(0)
elif codigo == 1:
    print(vetor)
elif codigo == 2:
    print(vetor[-1::-1])
else:
    print('Código Inválido.')
