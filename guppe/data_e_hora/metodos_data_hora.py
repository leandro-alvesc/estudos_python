"""
Métodos de Data e Hora
"""
import datetime

# Com now() podemos especificar um timezone
agora = datetime.datetime.now()
print(agora)

hoje = datetime.datetime.today()
print(hoje)

# Mudanças ocorrendo à meia noite combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)

# Dia da semana
print(manutencao.weekday())  # Começa em 0, sendo essa a segunda-feira

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto
print(agora.strftime('%d/%m/%Y'))
print(agora.strftime('%H:%M'))

# Usando TextBlob (pip install textblob)
from textblob import TextBlob

print(f"{agora.day} de {TextBlob(agora.strftime('%B')).translate(to='pt-br')} de {agora.year}")

# Transformando string para data
# nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy) ')
# print(datetime.datetime.strptime(nascimento, '%d/%m/%Y'))

# Somente hora
print(agora.time())

# Marcando tempo de execução com timeit
import timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=100000)
print(tempo)

# Teste com functools para saber se a função é performática
import functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))
