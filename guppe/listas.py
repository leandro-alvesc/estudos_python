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


# Fazemos acesso aos elementos de forma indexada

#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa (como uma roda, onde o final está ligado ao início)
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde

# Printar em for e while
for cor in cores:
    print(cor)
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Usando o enumerate para criar índice em lista
cores1 = list(enumerate(cores))
print(cores)
print(cores1)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
print(lista)


# Outros métodos não tão importantes mas também úteis
# Encontrar o índice de um elemento na lista
numeros = [5, 6, 5, 7, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9?
print(numeros.index(9))

# OBS: Caso não haja o elemento na lista será apresentado o erro ValueError
# print(numeros.index(22))

# OBS: Caso haja elemento duplicado, ele retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# OBS: Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1))  # Buscando a partir do índice 1
print(numeros.index(5, 2))  # Buscando a partir do índice 2
# print(numeros.index(5, 3))  # Buscando a partir do índice 3
# OBS: Caso não tenha esse elemento será apresentado ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o valor 8 entre os indices 3 e 6



# Revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmentro 'início'

lista = [1, 2, 3, 4]
print(lista[::])  # Pega todos os elementos
print(lista[1:])  # Iniciando do índice 1 e pegando todos os elementos restantes
print(lista[-3:])  # Iniciando do índice -3 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmentro 'fim'
print(lista[:2])  # Começa do índice 0, pega até o índice 2-1
print(lista[:4])  # Começa do índice 0, pega até o índice 4-1

print(lista[1:3])  # Começa do índice 1 e pega até o índice 3-1

# Trabalhando com slice de lista com o parâmetro 'passo'
print(lista[1::2])  # Começa em 1, vai até o final de 2 em 2

print(lista[::2])  # Começa em 0, vai até o final de 2 em 2


# Invertendo valores em uma lista
nomes = ['Junji', 'Ito']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Junji', 'Ito']
nomes.reverse()
print(nomes)

for nome in nomes:
    print(nome, end=" ")



# Soma, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # mínimo valor
print(len(lista))  # tamanho da lista


# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos quantidades diferentes para desempacotar do que variáveis para receber os valores teremos ValueError



# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)

print(lista)
print(nova)

# OBS: Veja que ao utilizarmso lista.copy() copiamos os dados para uma nova lista, mas elas ficaram totalmente
# independentes, ou seja, modificando uma não afeta a outra. Isso em Python é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

# OBS: Veja que utilizamso a cópia via atribuição, nesse caso os dados são copiados para a nova lista, porẽm
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas. Em Python, isso
# é chamado de Shallow Copy

"""