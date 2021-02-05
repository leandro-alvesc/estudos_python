# Função que converta graus C em F


def c_para_f(c):
    f = c * (9/5) + 32
    return f


graus = float(input('Temperatura em graus C: '))

print(c_para_f(graus))
