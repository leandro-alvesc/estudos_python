"""
Argumentos somente posicionais
"""
valor = '67.5'

print(float(valor))


def diz_oi_v1(nome):
    return f'Oi {nome}'


print(diz_oi_v1('João'))
print(diz_oi_v1(nome='João'))


def diz_oi_v2(nome, /):
    return f'Oi {nome}'


print(diz_oi_v2('José'))
# print(diz_oi_v2(nome='José'))


def diz_oi_v3(nome, /, mensagem='Oi'):
    return f'{mensagem} {nome}'


print(diz_oi_v3('Roberta', 'Bom dia'))
print(diz_oi_v3('Roberta', mensagem='Bom dia'))


def diz_oi_v4(nome, mensagem='Oi', /):
    return f'{mensagem} {nome}'


print(diz_oi_v4('Maria', 'Boa tarde'))
# print(diz_oi_v4('Roberta', mensagem='Bom dia'))


def diz_oi_v5(*, nome):
    return f'Olá {nome}'


print(diz_oi_v5(nome='Túlio'))
# print(diz_oi_v5('Túlio'))


def diz_oi_v6(nome, /, *, mensagem='Oi'):
    return f'{mensagem} {nome}'


# print(diz_oi_v6('Roberta', 'Bom dia'))
print(diz_oi_v6('Roberta', mensagem='Bom dia'))