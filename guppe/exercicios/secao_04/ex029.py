# Leia quatro notas, calcule a média aritmética e imprima o resultado
notas = []
soma = 0
for num in range(4):
    n = float(input(f'Insira a {num+1}o nota: '))
    notas.append(n)
    soma = soma + n

media = soma / len(notas)

print(f'A média das notas é: {media}')
