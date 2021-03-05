"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão.

variável := expressão
"""
print(nome := 'Emiliano')

cesta = []
while (fruta := input('Informe a fruta: ')) != 'sair':
    cesta.append(fruta)

print(cesta)
