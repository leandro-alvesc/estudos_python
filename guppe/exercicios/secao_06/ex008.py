# Ler 10 numeros e escrever o menor e o maior valor
maior = 0
menor = 0
for num in range(1, 11):
    val = int(input(f'Digite o {num}o valor: '))
    if num == 1:
        menor = val
        maior = val
    elif val < menor:
        menor = val
    elif val > maior:
        maior = val

print(f'O menor valor lido foi {menor} e o maior valor lido foi {maior}.')
