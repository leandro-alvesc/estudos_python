# 780.000,00 será dividido entre 3 ganhadores de um concurso. O primeiro receberá 46%, o segundo 32% e o terceiro
# o restante
total = 780_000.00
primeiro = total * 0.46
segundo = total * 0.32
terceiro = total - (primeiro + segundo)

print(f'O total do prêmio é R$ {total:,.2f}')
print(f'O primeiro lugar receberá R$ {primeiro:,.2f}')
print(f'O segundo lugar receberá R$ {segundo:,.2f}')
print(f'O terceiro lugar receberá R$ {terceiro:,.2f}')
