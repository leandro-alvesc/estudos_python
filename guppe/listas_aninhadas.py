"""
Listas Aninhadas - Nested Lists

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python temos as Listas
numeros = [1, 'b', 3.5, True, 5]

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

print(listas)

# Como fazemos para acessar os dados?

print(listas[0][1])  # Acesso ao número 2
print(listas[2][1])  # Acesso ao número 8
print(listas[2][-2])  # Acesso ao número 8


# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num, end=' ')
    print()


# List Comprehension
[[print(valor, end=' ') for valor in lista] for lista in listas]

"""
# Gerando um tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
