# Ler a nota e o número de faltas, escrever o conteito. Quando o aluno tem mais de 20 faltas ocorre redução de conceito
nota = float(input('Qual a nota do aluno? '))
faltas = int(input('Quantas faltas tem o aluno? '))
conceito = ''

if nota <= 3.9:
    conceito = 'E'
elif nota <= 4.9:
    conceito = 'D'
    if faltas > 20:
        conceito = 'E'
elif nota <= 7.4:
    conceito = 'C'
    if faltas > 20:
        conceito = 'D'
elif nota <= 8.9:
    conceito = 'B'
    if faltas > 20:
        conceito = 'C'
else:
    conceito = 'A'
    if faltas > 20:
        conceito = 'B'

print(f'Conceito: {conceito}')
