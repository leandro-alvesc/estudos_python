# Receber altura e peso e mostrar a classificação de acordo com a tabela
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilos: '))
clas = ''

if peso <= 60:
    if altura < 1.20:
        clas = 'A'
    elif altura <= 1.70:
        clas = 'B'
    else:
        clas = 'C'
elif peso <= 90:
    if altura < 1.20:
        clas = 'D'
    elif altura <= 1.70:
        clas = 'E'
    else:
        clas = 'F'
else:
    if altura < 1.20:
        clas = 'G'
    elif altura <= 1.70:
        clas = 'H'
    else:
        clas = 'I'

print(f'Sua classificação é {clas}')
