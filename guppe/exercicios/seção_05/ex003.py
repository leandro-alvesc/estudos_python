# Leia um numero, se for positivo calcule a raiz quadrada, se for negativo imprima o num ao quadrado
import math
num = float(input('Digite um número: '))

if num >= 0:
    rq = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {rq}.')
else:
    print(f'Número ao quadrado: {num ** 2}')
