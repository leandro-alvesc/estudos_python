"""
Manipulando Data e Hora

Python tem módulo built-in para se trabalhar com data e hora chamada datetime

# print(dir(datetime))

# Anos máximos e mínimos
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Data e hora atual
# print(datetime.datetime.now())

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()

print(inicio)

# Alterar o hoŕario para 16:0:0.0 ano 2011
inicio = inicio.replace(year=2011, hour=16, minute=0, second=0, microsecond=0)

print(inicio)
"""
import datetime

"""
Recebendo dados do usuário e convertendo em datetime
evento = datetime.datetime(2021, 4, 15, 0)

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
"""
agora = datetime.datetime.now()

# Acesso individual dos elementos de data e hora
print(agora.year)
print(agora.month)
print(agora.day)
print(agora.hour)
print(agora.minute)
print(agora.second)
print(agora.microsecond)
