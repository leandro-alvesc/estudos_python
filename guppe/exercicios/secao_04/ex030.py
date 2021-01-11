# Ler valor em real e cotação do dolar, imprimir o valor em dolar
real = float(input('R$: '))
cotacao = float(input('Informe a cotação do dólar: '))

dolar = real / cotacao

print(f'O valor em dólar é: ${dolar:.2f}')
