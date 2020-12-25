# Ler um numero int pos par N e imprimir todos os pares ate n em ordem decrescente
num = int(input('Ditire um número par: '))
if num % 2 == 0:
    for c in range(num, -1, -2):
        print(c)
else:
    print('O número digitado não é par.')
