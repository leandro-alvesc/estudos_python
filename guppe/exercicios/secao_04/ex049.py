# Ler o horario(hora, minuto e segundo) de inicio e a duração em segundos de uma exp biologica
# Resultar com o novo horário do término da mesma
hora_inicial = int(input('Digite a hora de inícial: '))
minuto_inicial = int(input('Digite o minuto inicial: '))
segundo_inicial = int(input('Digite o segundo inicial: '))
duracao = int(input('Digite a duração em segundos: '))

hora = duracao / 3600
resto = duracao % 3600
minuto = resto / 60
segundo = resto % 60

hora_final = hora_inicial + hora
minuto_final = minuto_inicial + minuto
segundo_final = segundo_inicial + segundo

if segundo_final > 59:
    segundo_final = segundo_final % 60
    minuto_final += segundo_final / 60

if minuto_final > 59:
    minuto_final = minuto_final % 60
    hora_final += minuto_final / 60

if hora_final > 23:
    hora_final = hora_final % 24

print(f'Hora de término: {hora_final:02.0f}:{minuto_final:02.0f}:{segundo_final:02.0f}')
