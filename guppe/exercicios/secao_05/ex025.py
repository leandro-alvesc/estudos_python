# Calcular equação de segundo grau (ax² + bx + c = 0), a variável a tem que ser diferente de 0
import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

r1 = 0
r2 = 0

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    r1 = -b / 2 * a
    print(f'Raiz única: {r1}')
else:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'Raiz 1: {r1}')
    print(f'Raiz 2: {r2}')
