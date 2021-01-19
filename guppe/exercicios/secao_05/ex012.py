# Ler um número inteiro, se for negativo escrever "Número inválido", se positivo calcular o logaritmo
import math

num = int(input('Digite um número inteiro positivo: '))

if num > 0:
    logaritmo = math.log(num)
else:
    print('Número inválido')

print(f'O logarítmo natural de {num} é: {logaritmo}')
