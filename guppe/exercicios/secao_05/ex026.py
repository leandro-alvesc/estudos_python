# Leia a distancia em Km e a quantidade de litros consumidos, retorne o Km/l e a mensagem correspondente
km = float(input('Digite a distância em Km: '))
lit = float(input('Digite a quantidade de litros consumidos: '))

consumo = km / lit

if consumo > 14:
    print(f'O consumo é {consumo:.2f} Km/l. Super Econômico!')
elif consumo > 8:
    print(f'O consumo é {consumo:.2f} Km/l. Econômico!')
else:
    print(f'O consumo é {consumo:.2f} Km/l. Venda o carro!')
