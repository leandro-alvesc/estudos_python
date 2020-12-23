# Leia um numero, se for positivo calcule a raiz quadrada, se for negativo mostre uma mensagem dizendo que
# número é inválido
import math
num = float(input('Digite um número: '))

if num >= 0:
    rq = math.sqrt(num)
    print(f'A Raiz Quadrada de {num} é {rq}.')
else:
    print('Número inválido')
