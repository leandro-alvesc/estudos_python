# Receber altura e sexo e mostrar o peso "ideal"
alt = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo: (m/f) ')

if sexo == 'm':
    peso = (72.7 * alt) - 58
    print(f'O peso "ideal" é {peso}Kg.')
elif sexo == 'f':
    peso = (62.1 * alt) - 44.7
    print(f'O peso "ideal" é {peso}Kg.')
else:
    print('Valores inválidos!')
