# Ler uma data e determinar se ela é válida
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if mes == 1 or mes == 3 or mes == 5 or 7 <= mes <= 8 or mes == 10 or mes == 12:
    if 1 <= dia <= 31:
        print(f'{dia:02}/{mes:02}/{ano:04}: Data válida.')
    else:
        print('Data inválida.')
elif 4 <= mes <= 11:
    if 1 <= dia <= 30:
        print(f'{dia:02}/{mes:02}/{ano:04}: Data válida.')
    else:
        print('Data inválida.')
elif mes == 2:
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        if 1 <= dia <= 29:
            print(f'{dia:02}/{mes:02}/{ano:04}: Data válida.')
        else:
            print('Data inválida.')
    else:
        if 1 <= dia <= 28:
            print(f'{dia:02}/{mes:02}/{ano:04}: Data válida.')
        else:
            print('Data inválida.')
else:
    print('Data inválida.')
