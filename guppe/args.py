"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer, isso significa que você poderá chamar de qualquer coisa, desde que
comece com *

Exemplo:
*xis
Mas por convenção, utilizamos *args para defini-lo

O Parâmetro *args coloca os valores extras informados como entrada em uma tupla (imutável).


# Exemplo


def soma_tudo(*args):
    return sum(args)


print(soma_tudo(2, 4, 5))
print(soma_tudo(1))
print(soma_tudo())
print(soma_tudo(5, 2, 3, 14, 5))
print(soma_tudo(2, 3))
print(soma_tudo(2, 4.56))


# Outro exemplo


def verifica_info(*args):
    if 'Kaori' in args and 'Sato' in args:
        return 'Bem-vinda, Kaori!'
    return 'Quem é você?'


print(verifica_info())
print(verifica_info(1, True, 'nada', '123'))
print(verifica_info('Kaori', 2, 4, 6, 'Sato'))
"""


def soma_tudo(*args):
    return sum(args)


numeros = [1, 2, 54, 6, 2, 8]

# Desempacotador
print(soma_tudo(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumentos
# uma coleção de dados. Saberá que precisará desempacotar esses dados.
