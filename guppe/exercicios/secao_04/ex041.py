# Ler o valor da hora de trabalho em reais e o número de horas trabalhadas no mês. Imprimir o valor a ser pago
# adicionando 10% sobre o valor calculado
valor_hora = float(input('Digite o valor da hora de trabalho: '))
hora = float(input('Digite o número de horas trabalhadas no mês: '))

total = (valor_hora * hora) + (valor_hora * hora) * 0.10

print(f'O total a ser pago é R$ {total:.2f}')
