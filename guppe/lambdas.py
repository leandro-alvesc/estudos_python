"""
Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções
anônimas.

# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar:
calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambdas com múltimpas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' joSe       ', ' golçALves     '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também
amar = lambda: 'Como não amar Python?'

# n = lambda x1, x2, ..., xn: <expressao>

print(amar())

# OBS: Se passarmos mais argumentos do que parâmetros esperados, teremos TypeError


# Outro exemplo (ordenação por sobrenome):
autores = ['Isaac Asimov', 'Junji Ito', 'Edgar Allan Poe', 'H. G. Wells', 'H.P. Lovecraft', 'Neil Gaiman']

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

"""
# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a Função:


def gerador_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c
    A Função retorna o lambda, podendo ser atribuído um parâmetro."""
    return lambda x: a * x ** 2 + b * x + c


teste = gerador_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(gerador_funcao_quadratica(2, 3, -5)(2))  # Sem precisar atribuir variável
print(gerador_funcao_quadratica.__doc__)
