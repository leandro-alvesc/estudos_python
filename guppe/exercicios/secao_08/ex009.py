# Função para receber raio e altura de um cilindro circular e retorne o volume


def vol_cilindo(altura, raio):
    volume = 3.1415 * (raio ** 2) * altura
    return volume


altura = float(input('Altura: '))
raio = float(input('Raio: '))

print(f'Volume: {vol_cilindo(altura, raio):.2f}')
