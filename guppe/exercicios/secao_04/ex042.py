# Receba o saãrio base de um funcionario, calcular e imprimir o salario a receber, sabendo que esse funcionario
# tem gratificação de 5% sobre o salario base, e pagando o imposto de 7% sobre o salario base
sal_base = float(input('Digite o salário-base: R$ '))

total = sal_base + (sal_base * 0.05) - (sal_base * 0.07)

print(f'O total a ser recebido é R$ {total:.2f}')
