# Função que receba dois valores e retorne o maior


def maior(x, y):
    if x > y:
        return x
    return y


n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

print(f'Maior: {maior(n1, n2)}')
