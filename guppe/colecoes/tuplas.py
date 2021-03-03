"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.
Existem duas diferenças básicas:
1- As tuplas são representadas por parênteses ()
2- As tuplas são imutáveis: ao criar uma tupla, ela não muda. Toda operação em uma tupla gera uma nova tupla.

print(type(()))


# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4, )  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula, e não pelos parênteses
(4) -> não é tupla
(4, ) -> é tupla
4, -> é tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla
tupla = ('Kendrick Lamar', 'DAMN.')

artista, album = tupla
print(artista)
print(album)

# OBS: Gera ValueError se colocarmos um número diferente de elementos para desempacotar

# Métodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)


# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)


# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)


# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))


# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
print('', end="| ")
for mes in meses:
    print(mes, end=" | ")
print()

print(meses[5])

# Iterar com while
i = 0
print('', end="| ")
while i < len(meses):
    print(meses[i], end=" | ")
    i += 1
print()


# Verificamos em qual índice um elemento está na tupla
print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado ValueError


# Slicing
# tupla[inicio:fim:passo]
print(meses[2:9:2])



"""
# Copiando uma tupla para outra
tupla = (1, 2, 3)

nova = tupla  # Na tupla não temos Shallow Copy

print(tupla)
print(nova)

outra = tupla + nova
print(outra)


# Por que utilizar tuplas?
# 1 - Tuplas são mais rápidas que listas
# 2 - Tuplas deixam seu código mais seguro
#        - Isso porque trabalhar com elementos imutáveis traz segurança para o código

