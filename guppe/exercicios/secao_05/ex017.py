# Ler um inteiro entre 1 e 12 e imprimir o mês correspondente
dia = int(input('Que mês estamos? '))

print('-'*30)
if dia == 1:
    print('Estamos em Janeiro')
elif dia == 2:
    print('Estamos em Fevereiro')
elif dia == 3:
    print('Estamos em Março')
elif dia == 4:
    print('Estamos em Abril')
elif dia == 5:
    print('Estamos em Maio')
elif dia == 6:
    print('Estamos em Junho')
elif dia == 7:
    print('Estamos em Julho')
elif dia == 8:
    print('Estamos em Agosto')
elif dia == 9:
    print('Estamos em Setembro')
elif dia == 10:
    print('Estamos em Outubro')
elif dia == 11:
    print('Estamos em Novembro')
elif dia == 12:
    print('Estamos em Dezembro')
else:
    print('Mês inexistente')
