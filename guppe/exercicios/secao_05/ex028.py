# Ler 3 numeros inteiros positivos e calcular a media de acordo com o escolhido
x = int(input('Digite a nota 1: '))
y = int(input('Digite a nota 2: '))
z = int(input('Digite a nota 3: '))

media = 0

opcao = input(f'Que fórmula deseja utilizar? \n(a) Geométrica \n(b) Poderada \n(c) Harmônica \n(d) Aritmética \n')

if opcao == 'a':
    media = (x * y * z) * (1 / 3)
elif opcao == 'b':
    media = (x + 2 * y + 3 * z) / 6
elif opcao == 'c':
    media = 1 / (1 / x + 1 / y + 1 / z)
elif opcao == 'd':
    media = (x + y + z) / 3
else:
    print('Não é uma opção válida.')

print(f'Média: {media}')
