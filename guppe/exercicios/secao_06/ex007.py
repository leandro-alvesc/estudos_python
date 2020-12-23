# Ler 10 inteiros positivos, ignorando não positivos e imprimir a média
soma = 0
cont = 0
for num in range(1, 11):
    val = int(input(f'Digite o {num}o valor: '))
    if val >= 0:
        soma = soma + val
        cont = cont + 1

media = soma / cont
print(f'A média é {media}.')
