# Escrever um programa que leia o código do produto escolhido do cardapio de uma lanchonete e a quantidade. Calcular o
# valor a ser pago por aquele lanche. Cada execução somente calcula um pedido

itens = [
    ('Cachorro Quente ', 100, 1.20),
    ('Bauru Simples   ', 101, 1.30),
    ('Bauru com Ovo   ', 102, 1.50),
    ('Hamburguer      ', 103, 1.20),
    ('Cheeseburguer   ', 104, 1.70),
    ('Suco            ', 105, 2.20),
    ('Refrigerante    ', 106, 1.00)
]

print('-' * 11 + ' MENU ' + '-' * 11)
print('ESPECIFICAÇÃO        CÓDIGO   PREÇO')
for n in range(0, len(itens)):
    for c in range(3):
        print(itens[n][c], end='      ')
    print()

print()
escolha = int(input('Qual o código do pedido? '))
qtd = int(input('Qual a quantidade? '))
for n in range(0, len(itens)):
    if itens[n][1] == escolha:
        print(f'PEDIDO:      {itens[n][0]}')
        print(f'PREÇO UN:    {itens[n][2]}')
        print(f'PREÇO TOTAL: {itens[n][2] * qtd}')
    else:
        print('Escolha Inválida')
        break
