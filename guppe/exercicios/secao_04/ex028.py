# Faça a leitura de 3 valores e apresente como resultado a soma dos quadrados dos três valores lidos
soma = 0
for num in range(1, 4):
    valor = float(input(f'Entre o {num}o valor: '))
    soma = soma + valor ** 2

print(f'A soma dos quadrados dos números digitados é {soma}.')
