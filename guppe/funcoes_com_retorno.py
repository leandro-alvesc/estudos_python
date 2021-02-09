"""
Funções com retorno

numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retorno de pop: {ret}')

ret_pr = print(numeros)  # não retorna nada

print(ret_pr)

OBS: Quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores devem utilizar a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
Podemos passar a execução da função para outras funções.


# Exemplo função sem retorno


# def quadrado_de_7():
#     print(7*7)


# Refatorando essa função para que retorne o valor


def quadrado_de_7():
    return 7*7


# Aqui foi criada uma variável para receber o retorno da função
ret = quadrado_de_7()
print(ret)

# Podemos fazer:
print(quadrado_de_7())


OBS: Sobre a palavra reservada return
    1- Ela finaliza a função, saindo da execução da função;
    2- Podemos ter em uma função, diferentes returns;
    3- Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores.

# Exemplo 1 - Ela finaliza a função, saindo da execução da função


def diz_oi():
    print('Execução antes do retorno.')
    return 'Oi'
    print('Execução após o return não acontece.')


print(diz_oi())



# Exemplo 2 - Podemos ter em uma função, diferentes returns


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)
print(outra_funcao())
print(type(outra_funcao()))



OBS: Erros comuns na utilização de retorno (não necessariamente erro, mas codificação desnecessária)
    - Utilização de else quando não é necessário, exemplo:
        - def eh_impar():
              numero = 5
              if numero % 2 != 0:
                  return True
              else:
                  return False
"""
# Criar uma função para jogar a moeda
from random import random


def jogar_moeda():
    # Gera um número pseudo-randomico entre 0 e 1
    # valor = random() -> não é necessário variável
    if random() < 0.5:
        return 'Cara'
    return 'Coroa'


if __name__ == '__main__':
    print(jogar_moeda())
