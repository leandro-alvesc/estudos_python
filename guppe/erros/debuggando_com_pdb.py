"""
Debuggando com PDB
PDB -> Python Debugger

OBS: A utilização do print() para debuggar é uma prática ruim
def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return 'Ocorreu um erro: {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse debug. Utilizando o debugger.
# Em Python podemos fazer isso em diferentes IDEs, como o PyCharm, ou utilizando o PDB - Python Debugger
# Exemplo com PyCharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return 'Ocorreu um erro: {err}'


print(dividir(4, 3))

# Exemplo 1 com o PDB - Python Debugger
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza debugging)

import pdb

nome = 'Kendrick'
sobrenome = 'Lamar'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
album = 'DAMN.'
final = nome_completo + ' tem o album ' + album
print(final)

# Exemplo 2 com o PDB - Python Debugger
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
nome = 'Kendrick'
sobrenome = 'Lamar'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
album = 'DAMN.'
final = nome_completo + ' tem o album ' + album
print(final)

# Pq utilizar esse formato? Quando é utilizado durante o desenvolvimento, pois é só apagar a linha.


# Exemplo 3 com o PDB - Python Debugger
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado
# como função built-in chamada de breakpoint()
nome = 'Kendrick'
sobrenome = 'Lamar'
breakpoint()
nome_completo = nome + ' ' + sobrenome
album = 'DAMN.'
final = nome_completo + ' tem o album ' + album
print(final)

"""
# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))
# OBS: Como os nomes das variáveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel
