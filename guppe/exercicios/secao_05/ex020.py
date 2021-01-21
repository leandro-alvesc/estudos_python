# Dado 3 valores, A, B, C, ferificar se podem ser valores dos lados de um triângulo e qual tipo: escaleno, isóscele, ou
# equilátero
a = float(input('Digite o lado a do triângulo: '))
b = float(input('Digite o lado b do triângulo: '))
c = float(input('Digite o lado c do triângulo: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b == c:
        print('Triângulo Equilátero.')
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('Não é um triângulo.')
