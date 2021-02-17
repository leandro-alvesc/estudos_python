# Receber a venda e calcular a comissão
venda = float(input('Entre o valor da venda: '))
comissao = 0

if venda < 20_000:
    comissao = 400 + (venda * 0.14)
elif venda < 40_000:
    comissao = 500 + (venda * 0.14)
elif venda < 60_000:
    comissao = 550 + (venda * 0.14)
elif venda < 80_000:
    comissao = 600 + (venda * 0.14)
elif venda < 100_000:
    comissao = 650 + (venda * 0.15)
else:
    comissao = 700 + (venda * 0.16)

print(f'Valor da comissão: {comissao:.2f}')
