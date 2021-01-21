# Ler um numero inteiro entre 100 e 999 e imprimir na saída cada um dos algarismos que compôem o número
num = int(input('Digite um número entre 100 e 999: '))

if 100 <= num <= 999:
    lista = ""
    for n in range(3):
        lista += str(num % 10)
        num //= 10
    for n in range(2, -1, -1):
        print(lista[n])
else:
    print('Número inválido.')
