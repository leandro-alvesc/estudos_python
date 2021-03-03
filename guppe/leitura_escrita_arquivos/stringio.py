"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos, o software precisa ter permissão:
    - Permissão de Leitura
    - Permissão de Escrita

StringIO -> Utilizado para ler e criar arquivos em memória.

"""
from io import StringIO

mensagem = 'Uma string qualquer'

# Podemos criar um aruqivo em memória com uma string inserida, ou vazio para inserir o texto depois
arquivo = StringIO(mensagem)

# Tendo o arquivo podemos utilizar os conceitos
print(arquivo.read())

# Escrevendo mais textos
arquivo.write(' Textos')

# Movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
