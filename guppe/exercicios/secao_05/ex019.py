# Verificar se um numero inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois
num = int(input('Digite um número: '))

if num % 3 == 0 and not num % 5 == 0:
    print('Número divisível por 3 e não por 5')
elif num % 5 == 0 and not num % 3 == 0:
    print('Número divisível por 5 e não por 3')
elif num % 3 == 0 and num % 5 == 0:
    print('Número divisível por 3 e por 5')
else:
    print('Número não divisível por 3 nem por 5')
