"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar o
cursor.


arquivo = open('texto.txt')

print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(57)
print(arquivo.read())


readline() -> Ler o arquivo linha a linha.
print(arquivo.readline())

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))



readlines() -> Coloca as linhas em uma lista

linhas = arquivo.readlines()
print(linhas)
print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador
e o programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhso com o arquivo, devemos fechar a conexão
utilizando a função close().

1- Abrir o arquivo
arquivo = open('texto.txt')

2- Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado (False)

3- Fechar o arquivo
arquivo.close()

print(arquivo.closed)  # True


# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos ValueError
"""
arquivo = open('texto.txt')

print(arquivo.read(57))

print(arquivo.read())  # Continua de onde parou o cursor

