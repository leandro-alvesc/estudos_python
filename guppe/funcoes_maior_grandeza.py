"""
Funções de Maior Grandeza - Higher Order Functions - HOF

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
como resultado, ou mesmo que podemos passar funções como argumentos para outras funções, e até criar variáveis
do tipo de funções em nossos programas.

OBS: Na seção de funções isso foi utilizado

Em Python as funções são First Class Citzen

# Exemplo - Definindo as funções


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(n1, n2, funcao):
    return funcao(n1, n2)


# Testando funções
print(calcular(4, 3, somar))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas (Inner Functions - Funções Internas)
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Vaza ', 'Chega mais '))
    return humor() + pessoa


# Testando
print(cumprimento('Kamila'))
print(cumprimento('José'))


# Retornando funções de outras funções
from random import choice


def faca_rir():
    def rir():
        return choice(('KKKKKKK', 'AUIHIUDSAHIUFHASJD', 'AHHAHAHAHHA'))
    return rir


rindo = faca_rir()
print(rindo())

"""
# Inner Functions (Nested Functions) podem acessar o escopo de funções mais externas
from random import choice


def faca_rir(mensagem):
    def rir():
        risada = choice(('KKKKKKK', 'AUIHIUDSAHIUFHASJD', 'AHHAHAHAHHA'))
        return f'{risada} {mensagem}'
    return rir


# Testando
rindo = faca_rir('ENGRAÇADO')

print(rindo())
print(rindo())
print(rindo())
