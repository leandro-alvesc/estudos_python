"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos

lista = [1, 55, 89, 22, 115, 90]
print(max(lista))  # 115

dicionario = {'a': 1, 'b': 55, 'c': 89, 'd': 22, 'e': 115, 'f': 90}
print(max(dicionario))  # f
print(max(dicionario.values()))  # 115

v1 = 3
v2 = 15
print(max(v1, v2))

print(max(1, 44, 66, 88))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c'))



min() -> Retorna o menor valor em um iterável ou o maior de dois ou mais elementos

lista = [1, 55, 89, 22, 115, 90]
print(min(lista))  # 1

dicionario = {'a': 1, 'b': 55, 'c': 89, 'd': 22, 'e': 115, 'f': 90}
print(min(dicionario))  # a
print(min(dicionario.values()))  # 1

v1 = 3
v2 = 15
print(min(v1, v2))

print(min(1, 44, 66, 88))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c'))



nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim
"""
musicas = [
    {"titulo": "HIGHEST IN THE ROOM", "tocou": 3},
    {"titulo": "DAMN.", "tocou": 8},
    {"titulo": "DEVASTATED", "tocou": 5},
    {"titulo": "goosebumps", "tocou": 2}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO - Imprima somente o título da música
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# OU
mais = max(musicas, key=lambda musica: musica['tocou'])
print(mais['titulo'])
menos = min(musicas, key=lambda musica: musica['tocou'])
print(menos['titulo'])

# DESAFIO 2 - Encontrar a musica mais e menos tocada sem utilizar max() min() e lambda
tocou = 0
mais = ''
menos = ''

for musica in musicas:
    if musica['tocou'] > tocou:
        tocou = musica['tocou']
        mais = musica['titulo']

for musica in musicas:
    if musica['tocou'] < tocou:
        tocou = musica['tocou']
        menos = musica['titulo']

print(mais)
print(menos)
