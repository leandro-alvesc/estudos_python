# Ler um número inteiro entre 1 e 7 e imprimir o dia da semana correspondente
dia = int(input('Que dia da semana estamos? '))

print('-'*30)
if dia == 1:
    print('Estamos no Domingo')
elif dia == 2:
    print('Estamos na Segunda-Feira')
elif dia == 3:
    print('Estamos na Terça-Feira')
elif dia == 4:
    print('Estamos na Quarta-Feira')
elif dia == 5:
    print('Estamos na Quinta-Feira')
elif dia == 6:
    print('Estamos na Sexta-Feira')
elif dia == 7:
    print('Estamos no Sábado')
else:
    print('Dia inexistente')
