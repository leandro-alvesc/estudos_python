# Ler salario e o valor da prestação do emprestimo, se for maior que 20% do salario, imprima Emprestimo não concedido
# se for menor, imprima Emprestimo Concedido
sal = float(input('Qual o salário? '))
emp = float(input('Qual o valor da prestação? '))

if emp <= (sal * 0.2):
    print('Empréstimo Concedido.')
else:
    print('Empréstimo não Concedido.')
