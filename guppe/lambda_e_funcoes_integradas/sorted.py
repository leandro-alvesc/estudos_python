"""
Sorted

OBS: Não confunda a função sorted() com sort(). O sort() só funciona em listas.

Podemos utilizar sorted() com qualquer iterável

Como o nome já diz, serve para ordenar.

# Exemplo
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior
print(numeros)

# OBS: O sorted() sempre retorna uma lista com os elementos do iteravel ordenados e NÃO altera o elemento principal

numeros = [6, 1, 8, 2]
# Adicionando parâmetros ao sorted
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))  # Do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "jose", "tweets": ["Amo gatos"]},
    {"username": "jao1", "tweets": []},
    {"username": "legolas", "tweets": ["Comi uma mandioquinha frita", "Hoje ta calor"]},
    {"username": "caronte", "tweets": []},
    {"username": "kekw", "tweets": []}
]

print(usuarios)

# Ordenando pelo username - Ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando por tweet
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


"""
# Outro exemplo
musicas = [
    {"titulo": "HIGHEST IN THE ROOM", "tocou": 3},
    {"titulo": "DAMN.", "tocou": 8},
    {"titulo": "DEVASTATED", "tocou": 5},
    {"titulo": "goosebumps", "tocou": 2}
]

# Menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
