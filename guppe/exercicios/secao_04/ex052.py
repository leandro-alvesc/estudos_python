# 3 amigos jogam na loteria, caso ganhem o premio deve ser repartido proporcionalmente.
# Ler qnt cada um investiu, o valor do premio e imprimir quanto cada um ganharia
premio = float(input('Digite o valor do prêmio: R$ '))
amg1 = float(input('Quanto o primeiro amigo apostou? R$ '))
amg2 = float(input('Quanto o segundo amigo apostou? R$ '))
amg3 = float(input('Quanto o terceiro amigo apostou? R$ '))

total = amg1 + amg2 + amg3
porc_amg1 = ((100 * amg1) / total) / 100
porc_amg2 = ((100 * amg2) / total) / 100
porc_amg3 = ((100 * amg3) / total) / 100

print(f'O primeiro amigo ganha R$ {(porc_amg1 * premio):.2f}\n'
      f'O segundo amigo ganha R$ {(porc_amg2 * premio):.2f}\n'
      f'O terceiro amigo ganha R$ {(porc_amg3 * premio):.2f}')
