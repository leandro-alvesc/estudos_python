# Altura do degrau de uma escada e a altura que o usuario deseja alcançar, mostrar quantos degraus deverá subir
altura = float(input('Qual é a algura total em metros? '))
altura_degrau = float(input('Qual é a altura do degrau em metros? '))

degraus = altura / altura_degrau

print(f'Você deverá subir {degraus:.2f} degraus.')
