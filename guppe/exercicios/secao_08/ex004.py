# Descobrir se o numero é quadrado perfeito
valor = int(input('Entre o número para descobrir se é quadrado perfeito: '))


def quad_perfeito(x):
    raiz = int(x ** (1/2))
    if raiz ** 2 == x:
        return f'Quadrado perfeito'
    return f'Não é quadrado perfeito'


print(quad_perfeito(valor))
# print(quad_perfeito(9))
