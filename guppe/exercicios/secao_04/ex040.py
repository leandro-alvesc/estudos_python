# Uma empresa contrata um encanador a R$30,00 por dia, solicitar o número de dias trabalhados e imprimir a quantia
# que deverá ser paga, descontando 8% de imposto de renda
dias = float(input('Digite a quantidade de dias trabalhados: '))

total = (dias * 30) - ((dias * 30) * 0.08)

print(f'A quantia líquida a ser paga é R$ {total:.2f}')
