# Função para cálculo do volume de uma esfera


def vol_esfera(raio):
    volume = (4/3) * 3.1415 * (raio ** 2)
    return volume


valor = float(input('Informe o raio: '))
print(f'O volume da esfera de raio {valor} é {vol_esfera(valor):.2f}')
