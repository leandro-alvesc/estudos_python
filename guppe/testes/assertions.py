"""
Assertions (Afirmações / Checagens / Questionamentos)

Em Python utilizamso a palavra reservada assert para realizar simples afirmações utilizadas nos testes

Utilizamos o assert em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None, e caso seja falsa levanta um erro do tipo AssertionError

# Podemos especificar opcionalmente um segundo argumento ou uma mensagem de erro personalizada
# A palavra assert pode ser utilizada em qualquer função ou código, não precisa ser exclusivamente nos testes

# ALERTA:
    Se um programa for executado com o parâmetro -O nenhum assertion será validado
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser posutivos'
    return a + b


# print(soma_numeros_positivos(5, 2))  # 6
# print(soma_numeros_positivos(-5, 1))  # AssertionError


def comer(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'batata frita'
    ], 'A comida precisa estar na lista'
    return f'Estou comendo {comida}'


# print(comer('pizza'))
# print(comer('alface'))
