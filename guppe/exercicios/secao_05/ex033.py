# Um produto vai sofrer aumento de acordo com a tabela, leia o preço antigo, calcule e escreva o preço novo e escreva
# a mensagem de acordo.
preco_antigo = float(input('Insira o preço antigo: '))
preco_novo = 0

if preco_antigo <= 50:
    preco_novo = preco_antigo + (preco_antigo * 0.05)
elif preco_antigo <= 100:
    preco_novo = preco_antigo + (preco_antigo * 0.10)
else:
    preco_novo = preco_antigo + (preco_antigo * 0.15)

if preco_novo <= 80:
    print(f'Preço novo: R${preco_novo:.2f}')
    print('Barato')
elif preco_novo <= 120:
    print(f'Preço novo: R${preco_novo:.2f}')
    print('Normal')
elif preco_novo <= 200:
    print(f'Preço novo: R${preco_novo:.2f}')
    print('Caro')
else:
    print(f'Preço novo: R${preco_novo:.2f}')
    print('Muito caro')
