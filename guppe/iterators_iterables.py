"""
Entendendo Iterators e Iterables

Iterator -> Um objeto que pode ser iterado, retorna um dado sendo um elemento por vez quando uma função next()
é chamada

Iterable -> Um objeto que irá retornar um iterator quando a função iter() for chamada.
"""
nome = 'Joseph'
numeros = [1, 2, 3, 4]

it1 = iter(nome)  # É um iterable, mas não um iterator
it2 = iter(numeros)  # É um iterable, mas não um iterator

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

