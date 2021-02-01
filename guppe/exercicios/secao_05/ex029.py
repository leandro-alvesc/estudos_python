# Faça uma prova matematica para crianças: soma numeros inteiros aleatorios 1 - 100. Mostrar as respostas corretas e
# quanto o aluno acertou
from random import randint

print('-' * 5 + '  Prova de Matemática  ' + '-' * 5)
print(randint(0, 100))

corretas = 0
a1 = []
a2 = []
r = []

for n in range(5):
    a1.append(randint(0, 100))
    a2.append(randint(0, 100))
    r.append(int(input(f'Pergunta {n+1} - Qual a soma de {a1[n]} + {a2[n]}? ')))
    if r[n] == a1[n] + a2[n]:
        corretas += 1

for n in range(5):
    print(f'Questão {n+1}: {a1[n]} + {a2[n]} = {a1[n] + a2[n]}')
    print(f'Sua resposta: {r[n]}')
    print()

print(f'Acertou {corretas} questões!')
