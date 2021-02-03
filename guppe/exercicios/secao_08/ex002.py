# Função para receber data atual dia mes e ano em inteiro e exibir por extenso


def data_extenso(d, m, a):
    if m == 1:
        return f'{d} de janeiro de {a}'
    elif m == 2:
        return f'{d} de fevereiro de {a}'
    elif m == 3:
        return f'{d} de março de {a}'
    elif m == 4:
        return f'{d} de abril de {a}'
    elif m == 5:
        return f'{d} de maio de {a}'
    elif m == 6:
        return f'{d} de junho de {a}'
    elif m == 7:
        return f'{d} de julho de {a}'
    elif m == 8:
        return f'{d} de agosto de {a}'
    elif m == 9:
        return f'{d} de setembro de {a}'
    elif m == 10:
        return f'{d} de outubro de {a}'
    elif m == 11:
        return f'{d} de novembro de {a}'
    elif m == 2:
        return f'{d} de dezembro de {a}'
    return f'Data Inválida'


print(data_extenso(3, 2, 2021))
