"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido mostre:
- O total a pagar com desconto de 10% a vista;
- O valor de cada parcela em 3x sem juros;
- Comissão do vendedor caso seja a vista (5% sobre o valor com desconto)
- Comissão do vendedor, caso a venda seja parcelada (5% sobre o valor total)
"""
valor = float(input('Insira o valor total: R$ '))

# Total a pagar com desconto de 10%:
tot_10 = valor - valor * 0.10

# Valor de cada parcela 3x
cada_parcela = valor / 3

# Comissao a vista
comi_vista = tot_10 * 0.05

# Comissao parcelado
comi_parc = valor * 0.05

print(f'Valor do produto: R$ {valor:.2f}\n'
      f'Total à vista: R$ {tot_10:.2f}\n'
      f'Parcelado: 3x de R$ {cada_parcela:.2f}\n'
      f'Comissão do Vendedor (à vista): R$ {comi_vista:.2f}\n'
      f'Comissão do Vendedor (parcelado): R$ {comi_parc:.2f}')
