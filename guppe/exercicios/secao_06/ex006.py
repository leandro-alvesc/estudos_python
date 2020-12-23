# Ler 10 numeros e imprimir a média
soma = 0
for num in range(1, 11):
    val = int(input(f'Digite o {num}o número: '))
    soma = soma + val
    # cont = cont + 1

media = soma / num
print(media)
