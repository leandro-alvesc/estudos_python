"""
Funções com Parâmetro (de entrada)
- Funções que recebem dados para serem processados dentro da mesma.

Pensando em um programa qualquer, geralmente temos:
    entrada -> processamento -> saída

Pensando em uma função, já sabemos que existem funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída.


# Refatorando uma função


def quadrado(n):
    return n ** 2


print(quadrado(7))  # Se não passar parâmetros, ocorre TypeError
print(quadrado(2))


def diz_oi(n):
    return 'oi, ' + n


nome = input('Qual seu nome? ')
print(diz_oi(nome))


# Refatorando outra função


def cantar_parabens(n):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Parabéns, {n}!')


cantar_parabens('João')


# Funções podem ter n parâmetros de entrada, ou seja, podem receber como entrada
# quantos parâmetros forem necessários, separados por vírgula.
# Exemplo:


def soma(a, b):  # a e b são parâmetros
    return a + b


def multiplica(a, b):
    return a * b


def outra(a, b, msg):
    return (a + b) * msg


print(soma(5, 6))  # 5 e 6 são argumentos
print(multiplica(5, 6))
print(outra(5, 6, 'lalala'))

# OBS: Se for informado um número errado de parâmetros ou argumentos, teremos TypeError


Erro comum na utilização do return:


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total  # Identar o return dentro do loop for, sairá da função no primeiro loop



lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
"""
# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Kendrick', 'Lamar'))

# Diferença entre PARÂMETROS e ARGUMENTOS
# - PARÂMETROS -> Variáveis declaradas na definição de uma função
# - ARGUMENTOS -> Dados passados durante a execução de uma função

# A ordem dos parâmetros importa!
nome = 'Kendrick'
sobrenome = 'Lamar'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nome dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.
print(nome_completo(nome='Kendrick', sobrenome='Lamar'))
print(nome_completo(sobrenome=sobrenome, nome=nome))
