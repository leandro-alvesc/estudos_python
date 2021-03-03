"""
Teste de Velocidade com Expressões Geradoras


def teste():
    for num in range(1, 10):
        yield num


g1 = teste()

print(g1)
print(next(g1))

g2 = (num for num in range(1, 10))

print(g2)
print(next(g2))
"""
# Realizando teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100_000_000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100_000_000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression: {gen_tempo}')
print(f'List Comprehension: {list_tempo}')
