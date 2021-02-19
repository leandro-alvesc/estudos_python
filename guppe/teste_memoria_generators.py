# Teste de memória com Generator

# Função com lista
def fib_lista(maximo):
    numeros = []
    a, b = 0, 1
    while len(numeros) < maximo:
        numeros.append(b)
        a, b = b, a + b
    return numeros


"""
# Teste 1 - 448.7MiB
for n in fib_lista(100000):
    print(n)
"""


def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 - 2.6MiB
for n in fib_gen(100000):
    print(n)
