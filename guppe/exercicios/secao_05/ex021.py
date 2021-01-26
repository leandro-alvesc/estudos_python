# Escrever um menu de opções. Ler a opção e executar a operação escolhida
print('Escolha a opção: ')
print('1 - Soma de 2 números')
print('2 - Diferença entre 2 números (maior pelo menor)')
print('3 - Produto entre 2 números')
print('4 - Divisão entre 2 números (o denominador não pode ser zero)')
op = int(input('Opção '))
while op < 1 or op > 4:
    print('Opção inválida')
    op = int(input('Opção '))

if op == 1:
    a = float(input('A: '))
    b = float(input('B: '))
    print(f'A soma é: {a + b}')
elif op == 2:
    a = float(input('A: '))
    b = float(input('B: '))
    if a > b:
        print(f'A diferença é: {a - b:.2f}')
    else:
        print(f'A diferença é: {b - a:.2f}')
elif op == 3:
    a = float(input('A: '))
    b = float(input('B: '))
    print(f'O produto é: {a * b:.2f}')
else:
    a = float(input('A: '))
    b = float(input('B: '))
    if b != 0:
        print(f'A divisão é: {a / b:.2f}')
    else:
        print('Denominador inválido')
