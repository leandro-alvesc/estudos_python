"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional

Exemplo de função onde a passagem de parâmetro seja opcional:
print('Python')
print()

Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(n):
    return n ** 2


print(quadrado(5))
print(quadrado())  # TypeError


Passando um parâmetro padrão:


def exponencial(n, pot=2):  # Parâmetro recebe valor padrão. Se houver argumento, ele será substituído
    return n ** pot


print(exponencial(5))  # Por padrão eleve ao quadrado
print(exponencial(2, 3))  # Eleva à potencia informada


# OBS: Em funções Python, os parâmetros com valors default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO:
def teste(num=2, potencia):  # teria que ser (potencia, num=2)
    return num ** potencia


# Outros exemplos


def soma(n1=1, n2=1):
    return n1 + n2


print(soma(4, 3))
print(soma(4))
print(soma())


# Exemplo mais complexo


def mostra_info(nome='José', instrutor=False):
    if nome == 'José' and instrutor:
        return f'Bem vindo, instrutor {nome}!'
    elif nome == 'José':
        return 'Achei que fosse o instrutor...'
    return f'Olá, {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info('Kate'))

Por que utilizar parâmetros com valor deafult?
 - Permite ser mais flexíveis nas funções
 - Evita erros com parâmetros incorretos
 - Permite trabalhar com exemplos mais legíveis

Quais tipos de dados podemos utilizar como valores default para parâmetros?
 - Qualquer tipo de dado
     - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc



# Exemplo de funções como parâmetros


def soma(n1, n2):
    return n1 + n2


def mat(n1, n2, fun=soma):
    return fun(n1, n2)


def subtracao(n1, n2):
    return n1 - n2


print(mat(2, 3))
print(mat(2, 3, subtracao))


# Escopo - Evitar problemas e confusões
# Variáveis globais
# Variáveis locais

instrutor = 'José'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    saudacao = 'Tudo bem?'
    return f'Oi {instrutor}! {saudacao}'


print(diz_oi())
print(saudacao)  # NameError - Variável local não é utilizada fora do bloco em que está

# Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência


# ATENÇÃO  com variáveis globais (Se puder evitar, evite)
total = 0


def incrementa():
    total = total + 1  # UnboundLocalError (A variável local está sendo utilizada sem ter sido inicializada)
    return total


print(incrementa())

COMO UTILIZAR:
total = 0


def incrementa():
    global total  # Avisando que queremos utlizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())


# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Não é uma variável local dentro, nem global, então utilizamos nonlocal
        contador = contador + 1
        return contador

    return dentro()


print(fora())
print(dentro())  #NameError

"""
