"""
Calcular a nota final a partir de 3 notas de 0 a 10 com os pesos:
trabalho de lab: 2
avaliação semestral: 3
exame final: 5

De acordo com o resultado mostre na tela se o aluno está reprovado (entre 0 e 2.9), de rec (3 e 4.9) ou se foi aprovado
"""
nome = input('Qual o nome do aluno? ')
trab = float(input(f'Qual foi a nota de {nome} no Trabalho de Laboratório (peso 2)? '))
aval = float(input(f'Qual foi a nota de {nome} na Avaliação Semestral (peso 3)? '))
exam = float(input(f'Qual foi a nota de {nome} no Exame Final (peso 5)? '))

media = (trab * 2 + aval * 3 + exam * 5) / (2 + 3 + 5)

print(f'A média de {nome} foi: {media:.2f}')

if media <= 2.9:
    print('Aluno REPROVADO.')
elif media <= 4.9:
    print('Aluno DE RECUPERAÇÃO.')
else:
    print('Aluno APROVADO.')
