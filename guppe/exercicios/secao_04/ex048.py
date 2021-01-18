# Ler um valor inteiro em segundos e imprimir em horas minutos e segundos
segundos_total = int(input('Digite o valor em segundos: '))

horas = segundos_total / 3600
resto = segundos_total % 3600
minutos = resto / 60
segundos = resto % 60

print(f'{horas:02.0f}:{minutos:02.0f}:{segundos:02.0f}')
