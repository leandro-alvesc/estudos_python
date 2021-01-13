# Ler um numero inteiro e imprimir a soma do sucessor de seu triplo com o antecessor de seu dobro
num = int(input('Digite um número inteiro: '))

n1 = num * 3 + 1
n2 = num * 2 - 1

print(f'A soma do sucessor do triplo de {num} com o antecessor do dobro do mesmo é: {n1+n2}')
