# Programa para o usuário digitar 10 valores e some
soma = 0
for num in range(1,11):
    val = int(input(f'Digite o {num}o valor: '))
    soma = soma + val

print(f'A soma de todos os valores é {soma}.')
