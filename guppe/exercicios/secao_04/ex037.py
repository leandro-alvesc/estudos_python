# Ler o valor de um produto e imprimir o valor com desconto de 12%
val = float(input('Digite o valor do produto: '))

val_desc = val - (val * 0.12)

print(f'O valor com desconto é R${val_desc:.2f}')
