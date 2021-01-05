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

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Podemos facilmente inverter uma lista através do reverse()
# lista1.reverse()
# lista2.reverse()

# Ou podemos utilizar o slice
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))
print(len(lista2))

# Podemos remover o último elemento de uma lista
# OBS: O pop não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita desse índice serão deslocados para a esquerda
# OBS: Se não houver elemento no índice informado teremos o erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos na lista
novo = [1, 2, 3]
print(novo)
novo = novo * 3
print(novo)

# Podemos converter uma string para uma lista
# Exemplo 1
nome = 'Kendrick Lamar'
print(nome)
nome = nome.split()
print(nome)
# OBS: Por padrão o split separa os elementos  da lista pelo espaço entre elas

# Exemplo 2
nome = 'Kendrick,Lamar'
print(nome)
nome = nome.split(',')
print(nome)
# OBS: Podemos especificar o separador do split, no caso desse exemplo sendo a vírgula

# Convertendo uma lista em uma string
lista6 = ['Kendrick', 'Lamar']
print(lista6)
# Abaixo estamos falando: Pegue a lista6, coloque espaço entre cada elemento e transforme em string
nome = ' '.join(lista6)
print(nome)
# Abaixo estamos falando: Pegue a lista6, coloque $ entre cada elemento e transforme em string
nome = '$'.join(lista6)
print(nome)

# Podemos colocar qualquer tipo de dado, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Kaori', 'j', [1, 2, 3], 4251246123]
print(lista6)


# Iterando sobre listas
# Exemplo 1 - utilizando for
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    produto = input("Adicione um produto na lista ou digite 'sair' para sair: ")
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Utilizando variáveis em listas
numeros = [1, 2, 3]
print(numeros)

num1 = 1
num2 = 2
num3 = 3

numeros = [num1, num2, num3]
print(numeros)


"""
type([])

lista1 = [1, 2, 99, 44, 15, 4, 5, 1, 42, 27]

lista2 = ['K', 'a', 'o', 'r', 'i']

lista3 = []

lista4 = list(range(11))

lista5 = list('Kaori')

