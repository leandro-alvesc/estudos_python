"""
Reduce

OBS: A partir do Python 3+ a função reduce() não é mais uma funcção integrada (built-in). Agora temos que importar
e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível.

Para entender o reduce()
# Imagine que você tem uma coleçao de dados:
dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # Aplica a função passadno o resultado do passo1 mais o terceiro elemento e guarda o res
    Isso é repetido até o final

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. Ao final
da execução retorna o resultado final.

Alternativamente poderíamos ter a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""
# Como utilizar
# Multiplicar todos os números de uma lista
from functools import reduce

dados = [2, 3, 4, 6, 7, 1, 3, 55, 23, 9]

# Para utilizar o reduce() precisamos de uma função que receba dois parâmetros
# multi = lambda x, y: x * y

res = reduce(lambda x, y: x * y, dados)
print(res)

# Utilizando um loop normal
res = 1
for n in dados:
    res = res * n

print(res)
