"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobreescreve caso já exista
x -> Abre para escrita somente se o arquivo não existir, se existir gera FileExistsError
+ -> Abre para modo de atualização.

http://docs.python.org/3/library/functions.html#open

# Exemplo x:
try:
    with open('novo.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe.')


# Exemplo a:
with open('novo.txt', 'a') as arquivo:
    while True:
        teste = input('O que deseja adicionar? ')
        if teste != 'sair':
            arquivo.write(teste + '\n')
        else:
            break

"""
