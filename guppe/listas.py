"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nessas linguagens se você criar um array do tipo int e com tamanho 5, este array SEMPRE
    será do tipo inteiro e SEMPRE no máximo 5 valores.

Em Python:
- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
"""
type([])

lista1 = [1, 2, 99, 44, 15, 4, 5, 1, 42, 27]

lista2 = ['K', 'a', 'o', 'r', 'i']

lista3 = []

lista4 = list(range(11))

lista5 = list('Kaori')

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('a'))

# Adicionar elementos em listas


# Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: com append só conseguimos adicionar 1 elemento por vez
# lista1.append(1, 2, 3) # Erro

lista1.append([1, 2, 3])  # Coloca a lista como elemento único
print(lista1)

if [1, 2, 3] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([1, 2, 3])  # Coloca cada elemento da lista como valor adicional
print(lista1)
