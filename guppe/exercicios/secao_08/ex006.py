# Receber 3 numeros inteiros como parâmetro representando horas minutos e segundos e converter em segundos


def segundos(h, m, s):
    sec = s + (m * 60) + (h * 3600)
    return sec


hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))

print(f'O valor de {hora:02}:{minuto:02}:{segundo:02} em segundos é {segundos(hora, minuto, segundo)}')
