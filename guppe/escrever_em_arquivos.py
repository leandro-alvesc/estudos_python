"""
Escrevendo em Arquivos


# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita, apenas ler. Da mesma forma se abrirmos um
arquivo para escrita, não podemos ler, somente escrever.
Ao abrir um arquivo para escrita, o arquivo é criado no sistema.
Para escrevermos dados em um arquivo, após abrir o arquivo, utilizamos a função write() que recebe uma string como
parâmetro, caso contrário teremos TypeError.

Caso o arquivo já exista, o arquivo será sobrescrito.
"""
teste = input('O que deseja escrever 10 vezes? ')
# Exemplo de escrita - Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrevendo dados em arquivo.\n')
    arquivo.write('Alterando os dados\n')
    arquivo.write('Linha\n')
    arquivo.write(f'{teste}\n' * 10)
    while True:
        texto = input('O que mais deseja escrever? (sair para finalizar) ')
        if texto != 'sair':
            arquivo.write(texto)
            arquivo.write('\n')
        else:
            break
    arquivo.write('Bye')
