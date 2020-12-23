# Ler duas notas e exibir a média, a nota deve ser entre 0.0 e 10.0
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if (nota1 > 10.0 or nota2 > 10.0) or (nota1 < 0.0 or nota2 < 0.0):
    print('Nota Inválida.')
else:
    media = (nota1 + nota2) / 2
    print(f'A média entre as duas notas é {media}.')
