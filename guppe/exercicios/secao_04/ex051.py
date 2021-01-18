# Ler as coordenadas x e y dos pontos no R² e calcule sua distância de origem (0,0)
import math

x = float(input('Digite o valor da coordenada de X no ponto 1: '))
y = float(input('Digite o valor da coordenada de Y no ponto 1: '))

dist1 = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print(f'Distância do ponto 1 da origem (0,0): {dist1}')
