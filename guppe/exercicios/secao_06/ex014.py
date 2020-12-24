# Ler um numero int pos impar N e imprimir todos os pares ate ;n em ordem crescente
num = int(input('Ditire um número ímpar: '))
if num % 2 == 1:
    for c in range(1, num + 1, 2):
        print(c)
else:
    print('O número digitado não é ímpar.')
