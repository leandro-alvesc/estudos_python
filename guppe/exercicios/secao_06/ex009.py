# Ler um número inteiro N e depois imprima os N primeiros numeros naturais impares
n = int(input('Digite um número inteiro N: '))
for num in range(1, n + 1):
    if num % 2 == 1:
        print(num)
