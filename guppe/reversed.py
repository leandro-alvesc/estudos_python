"""
Reversed

OBS: Não confudir com a função reverse() que estudamos nas listas.

A função reversed() retorna um iteravel chamado List Reverse Iterator
"""
# Exemplo
lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter para uma lista, tupla ou conjunto
# Lista
print(list(reversed(lista)))
# Tupla
print(tuple(reversed(lista)))
# Set - Não define ordem
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Kendrick Lamar'):
    print(letra, end='')

print()
# O mesmo sem o uso do for
print(''.join(list(reversed('Kendrick Lamar'))))

# Fazer mais fácil com slice de strings
print('Kendrick Lamar'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):  # Como se fosse range(9, -1, -1)
    print(n)


