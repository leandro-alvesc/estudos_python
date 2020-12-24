# Ler um numero int positivo N e imprimir todos os numeros naturais de 0 a N em ordem decrescente
num = int(input('Digite um número inteiro positivo: '))
for c in range(num, -1, -1):
    print(c)
