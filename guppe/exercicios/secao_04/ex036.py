# Ler a altura e o raio de um cilindro e imprimir o volume
alt = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))

vol = 3.141592 * (raio ** 2) * alt

print(f'O volume do cilindro é: {vol:.2f}')
