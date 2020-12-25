# Ler uma quantidade de numero, imprimir o maior e quantas vezes o maior foi lido
qtd = int(input('Digite a quantidade de números a serem lidos: '))
maior = 0
qtmaior = 1

for c in range(1, qtd + 1):
    n = int(input(f'Digite o {c} número: '))
    if n > maior:
        maior = n
        qtmaior = 1
    elif n == maior:
        qtmaior += 1

if qtmaior == 1:
    print(f'O maior número foi {maior} e foi digitado {qtmaior} vez.')
else:
    print(f'O maior número foi {maior} e foi digitado {qtmaior} vezes.')
