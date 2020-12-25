# Ler um numero int positivo n e calcule a soma dos n primeiros números naturais
n = int(input('Digite um número inteiro positivo: '))
soma = 0
for c in range(0, n + 1):
    soma = soma + c

print(soma)
