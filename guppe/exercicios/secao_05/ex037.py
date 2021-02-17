# Estacionamento, chegada e partida de acordo com a tabela. O valor não passa de 24 horas
hora_inicial = int(input('Hora da chegada: '))
minuto_inicial = int(input('Minuto da chegada: '))

hora_final = int(input('Hora da partida: '))
minuto_final = int(input('Minuto da partida: '))

diff_hora = 0
diff_minuto = 0

valor = 0

if hora_inicial > 23 or hora_final > 23 or minuto_final > 59 or minuto_inicial > 59:
    print('Hora inválida.')
else:
    if hora_inicial <= hora_final:
        diff_hora = hora_final - hora_inicial
    else:
        diff_hora = (hora_final + 24) - hora_inicial
    if minuto_inicial <= minuto_final:
        diff_minuto = minuto_final - minuto_inicial
    else:
        diff_hora -= 1
        diff_minuto = (minuto_final + 60) - minuto_inicial
    if diff_minuto == 60:
        diff_hora += 1
        diff_minuto = 0

print(f'Total: {diff_hora:02}:{diff_minuto:02}')

min_total = (diff_hora * 60) + diff_minuto
cont = 0

if min_total <= 120:
    if min_total / 60 <= 1:
        cont = 1
    else:
        cont = 2
    valor = cont
elif min_total <= 240:
    if min_total / 60 <= 3:
        cont = 1
    else:
        cont = 2
    valor = 2 + (cont * 1.40)
else:
    for n in range(5, 25):
        if min_total / 60 <= n:
            cont = n - 4
            break
    valor = 4.80 + (2 * cont)

print(f'Total a pagar: R${valor:.2f}')
