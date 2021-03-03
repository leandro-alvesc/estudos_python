"""
Módulo Random e o que são módulos
- Em Python, módulos são outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios

# OBS: Existem duas formas de se utilizar um módulo ou função
# OBS: Para utilizar a função, colocamos o nome do pacote e o nome da função separados por ponto.
# OBS: Não confundir o pacote random com a função random()

# Forma 1 - Importando o módulo inteiro

import random

print(random.random())

# random() -> gera um número pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import do módulo inteiro, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis. Caso saiba quais funções precisa utilizar, essa forma não é a melhor, e sim
# a Forma 2

# Forma 2 - Importando uma função específica do mõdulo (Forma recomendada)
# OBS: Nesse caso não é preciso declarar o módulo, separando por ponto da função.

from random import random
# Importar a função random do módulo random
for i in range(10):
    print(random())

# uniform() -> gerar um número pseudo aleatório entre os valores estabelecidos
from random import uniform
for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído

# randint() -> gera valores pseudo-aleatórios entre os valores estabelecidos
from random import randint
for i in range(6):
    print(randint(1, 61), end=', ')

# choice() -> mostra um valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(choice('Olá mundo'))

"""
# shuffle() -> função de embaralhar dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas)

print(cartas[0])

# print(cartas.pop())
