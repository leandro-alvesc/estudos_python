# Escrever um programa que receba a idade do nadador e classificar nas categorias
idade = int(input('Digite a idade do nadador: '))

if idade > 17:
    print(f'CATEGORIA: Sênior')
elif idade > 13:
    print(f'CATEGORIA: Juvenil B')
elif idade > 10:
    print(f'CATEGORIA: Juvenil A')
elif idade > 7:
    print(f'CATEGORIA: Infantil B')
elif idade > 4:
    print(f'CATEGORIA: Infantil A')
else:
    print(f'Muito novo para competir')
