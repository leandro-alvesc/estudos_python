"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy hh:mm:ss.ms
data_final = dd/mm/yyyy hh:mm:ss.ms

delta = data_final - data_inicial
"""
import datetime

data_inicial = datetime.datetime.now()

data_final = datetime.datetime(2021, 8, 11, 12, 0)

# calculando o delta
tempo = data_final - data_inicial

# print(type(tempo))
# print(repr(tempo))

print(tempo)
print(f'Faltam {tempo.days} dias e {(tempo.seconds // 60) // 60} horas.')

print('\nBoleto')
compra = datetime.datetime.now()

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento = compra + regra_boleto
print(vencimento)
