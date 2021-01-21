# Mostrar um menu com 4 opções de operações matematicas. O usuário escolhe uma das opções e o programa pede 2 valores
# para realizar, mostrando o resultado e saindo
print('-'*14 + 'MENU' + '-'*14)
print('Escolha uma das opções abaixo: ')
print('1- Soma            2- Subtração')
print('3- Multiplicação   4- Divisão')
print('-'*32)

op = int(input('Qual operação deseja efetuar? '))
while op < 1 or op > 4:
    print('Opção inválida...')
    op = int(input('Qual operação deseja efetuar? '))


n1 = float(input('Digite o valor do primeiro número: '))
n2 = float(input('Digite o valor do segundo número: '))

if op == 1:
    print(f'A soma entre os dois é: {n1 + n2:.2f}')
elif op == 2:
    print(f'A subtração entre os dois é: {n1 - n2:.2f}')
elif op == 3:
    print(f'A multiplicação entre os dois é: {n1 * n2:.2f}')
else:
    print(f'A divisão entre os dois é: {n1 / n2:.2f}')
