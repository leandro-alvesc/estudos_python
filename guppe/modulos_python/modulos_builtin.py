"""
Trabalhando com Módulos Built-In

# Utilizando alias(apelidos) para módulos/funções
# 1
import random as rdm

print(rdm.random())

# 2
from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

# Podemos importar todas as funções de um módulo utilizando o *
from random import *
# import random -> diferente, pois quando importa * não é necessário usar o nome do modulo separado por ponto

print(random())

"""
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random as rdm,
    randint as rdi,
    shuffle as shf,
    choice as chc
)

print(rdm())
print(rdi(1, 55))

lista = [1, 2, 3, 4]
shf(lista)
print(lista)

print(chc('Hello World'))
