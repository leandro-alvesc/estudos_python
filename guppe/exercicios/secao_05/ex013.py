# Calcular a média ponderada das notas de 3 provas. A primeira e a segunda tem peso 1 e a terceira tem peso 2
# Mostrar a média e se foi aprovado (acima de 60 pontos)
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota(peso 1): '))
n2 = float(input('Digite a segunda nota(peso 1): '))
n3 = float(input('Digite a terceira nota(peso 2): '))

media = (n1 * 1 + n2 * 1 + n3 * 2) / (1 + 1 + 2)

print(f'A média de {nome} foi {media:.2f}.')
if media > 60:
    print('APROVADO')
else:
    print('REPROVADO')
