# Calcule e mostre a soma dos 50 primeiros números pares
soma = 0
c = 1
num = 0
while c <= 50:
    num += 2
    soma += num
    c += 1

print(f'A soma dos 50 primeiros números pares é: {soma}.')
