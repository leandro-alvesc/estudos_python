# Ler um número inteiro maior que 0 e devolver a soma de todos seus algarismos
# Ex: 251 = 8 (2 + 5 + 1)
# Se o número lido não for maior que 0 retornar "Número Inválido"

# Opção 1:
"""
num = int(input("Digite um número maior que 0: "))
soma = 0
if num > 0:
    while num > 0:
        resto = num % 10
        num = num // 10
        soma = soma + resto
else:
    print("Número inválido!")

print(f'A soma dos algarismos é: {soma}')

"""

# Opção 2:
num = input("Digite um número maior que 0: ")
soma = 0
i = 0
if int(num) > 0:
    while i < len(num):
        soma = soma + int(num[i])
        i = i + 1

print(soma)
