"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() recebe 2 parâmetros, sendo uma função e um iterável
res = filter(lambda valor: valor > media, dados)
print(res)
print(type(res))
print(list(res))

print(list(res))  # Assim como no map, os dados são excluídos da memória após a utilização

# Remoção de dados faltantes
paises = ['', 'Argentina', 'Brasil', '', 'Chile', '', 'Venezuela', '', '', 'Colombia', 'Cuba']

print(paises)

# res = filter(lambda pais len(pais) > 0, paises)
res = filter(None, paises)

print(list(res))

# Diferença entre map() e filter() é:
# map() -> recebe 2 parâmetros: uma função e um iterável; retorna um obj mapeando a função para cada elemento
# filter() -> recebe 2 parâmetros: uma função e um iterável; retorna um obj filtrando elementos de acordo com a função


# Exemplo mais complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "jose", "tweets": ["Amo gatos"]},
    {"username": "jao1", "tweets": []},
    {"username": "legolas", "tweets": ["Comi uma mandioquinha frita", "Hoje ta calor"]},
    {"username": "caronte", "tweets": []},
    {"username": "kekw", "tweets": []}
]
print(usuarios)

# Filtrar os usuários inativos no Twitter

# Forma 1
# inativos = list(filter(lambda user: len(user["tweets"]) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda user: not user["tweets"], usuarios))

print(inativos)
print('Lista de usuários inativos: ' + str([inativo["username"] for inativo in inativos]))
"""
# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
