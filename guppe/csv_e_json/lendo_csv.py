"""
Lendo arquivos CSV

CSV - Comma Separated Values

# Separador por vírgula
1, 2, 3, 4, 5

"oi", "python", "ola"

# Separador por ponto e vírgula
1, 2, 3, 4, 5

"oi", "python", "ola"

# Separador por espaço
1 2 3 4 5

"oi" "python" "ola"


# Possível de se trabalhar, porém não é o ideal (trabalhoso)
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

# A Linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts
    - Com outro separador, basta acrescentar um parâmetro. (arquivo, delimiter=';')

# Reader
from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no país {linha[1]} e mede {linha[2]}cm')
"""
# DictReader
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no país {linha['País']} e mede {linha['Altura (em cm)']}cm")
