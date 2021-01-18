# Ler o salario do funcionario e imprimir o salario com aumento de 25%
salario = float(input('Digite o salário do funcionário: '))

novo = salario + (salario * 0.25)

print(f'O salário com aumento é R${novo:.2f}')
