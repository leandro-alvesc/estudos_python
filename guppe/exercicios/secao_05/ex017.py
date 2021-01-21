# Calcular e mostrar a área de um trapézio, a base maior e base menor devem ser numeros maiores que 0
base_maior = float(input('Informe a base maior: '))

while base_maior <= 0:
    print('Valor inválido. Digite novamente.')
    base_maior = float(input('Informe a base maior: '))

base_menor = float(input('Informe a base menor: '))

while base_menor <= 0:
    print('Valor inválido. Digite novamente.')
    base_menor = float(input('Informe a base menor: '))

altura = float(input('Informe a altura: '))

while altura <= 0:
    print('Valor inválido. Digite novamente.')
    altura = float(input('Informe a altura: '))

area = ((base_maior + base_menor) * altura) / 2

print(f'A área do trapézio é: {area}')
