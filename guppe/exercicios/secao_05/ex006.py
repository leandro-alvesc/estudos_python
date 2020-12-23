# Faça um programa que receba dois números e mostre qual deles é maior com sua diferença
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    res = num1 - num2
    print(f'O primeiro número ({num1}) é maior que o segundo número ({num2}).')
    print(f'A diferença entre os dois é de {res}')
else:
    res = num2 - num1
    print(f'O segundo número ({num2}) é maior que o primeiro número ({num1}).')
    print(f'A diferença entre os dois é de {res}')
