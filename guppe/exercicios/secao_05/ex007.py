# Receba 2 numeros e mostre o maior, se forem iguais imprima Números Iguais
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número ({num1}) é maior que o segundo ({num2}).')
elif num1 == num2:
    print(f'O primeiro número ({num1}) é igual ao segundo ({num2}).')
else:
    print(f'O primeiro número ({num1}) é menor que o segundo ({num2}).')
