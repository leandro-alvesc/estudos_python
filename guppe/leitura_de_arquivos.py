"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utlizamos a função integrada open()

open() -> Na forma mais simples de utilização, passamos apenas um parâmetro de entrada, que é o nome
do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão a função open() abre o arquivo para leitura. Esse arquivo deve existir
ou teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
mode r -> Modo de Leitura

"""
arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura devemos utilizar a função read()

retorno = arquivo.read()

print(type(retorno))
print(retorno)

# print(arquivo.read())

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor
# funciona como o cursor quando estamos escrevendo
# A função read() lê to/do o conteúdo do arquivo, posicionando o cursor ao final, fazendo com que
# se executada novamente, não imprima nada.
