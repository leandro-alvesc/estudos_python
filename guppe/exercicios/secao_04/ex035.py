# Receber a e b (catetos) e calcular a hipotenusa

import math

a = float(input('Digite o cateto a: '))
b = float(input('Digite o cateto b: '))

hip = math.sqrt((a**2) + (b**2))

print(f'O valor da hipotenusa é: {hip:.2f}')
