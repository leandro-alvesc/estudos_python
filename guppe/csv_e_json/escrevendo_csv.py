"""
Escrevendo em arquivos CSV

writer() -> Método para criação
writerow() -> Escreve uma linha

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    mais = None
    escritor_csv.writerow(['Título', 'Gênero', 'Ano'])
    while mais != 'n':
        filme = input('Informe o nome: ')
        genero = input('Informe o gênero: ')
        ano = input('Informe o ano: ')
        escritor_csv.writerow([filme, genero, ano])
        mais = input('Deseja adicionar mais? (s/n) ')
"""
from csv import DictWriter

# DictWritter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Ano']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    mais = None
    while mais != 'n':
        filme = input('Informe o nome: ')
        genero = input('Informe o gênero: ')
        ano = input('Informe o ano: ')
        escritor_csv.writerow({"Título": filme, "Gênero": genero, "Ano": ano})
        mais = input('Deseja adicionar mais? (s/n) ')
