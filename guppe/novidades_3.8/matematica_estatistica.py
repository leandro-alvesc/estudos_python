import math
import statistics
# math.prod -> retorna o produto de um container numérico
nums_v1 = [2, 3, 5, 1]
nums_v2 = (2, 3, 5, 1)
nums_v3 = {2, 3, 5, 1}

# 2 * 3 * 5 * 1
print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.prod(nums_v3))
print()

# math.isqrt -> retorna a parte inteira da raiz quadrada de um numero
print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(15))
print(math.sqrt(15))
print()

# math.dist -> retorna a distância euclidiana entre dois pontos
# Ponto 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 4, 1)

# Ponto 2D
p2d1 = [12, 4]
p2d2 = [3, 5]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))
print()

# math.hypot -> retorna a hipotenusa ou norma eucludiana
print(math.hypot(*p3d1))
print(math.hypot(*p2d1))

# Estatística
# statistics.fmean - calcula a média de números reais
valores = [1.44, 2.45, 6.33]
valores_int = [1, 4, 2, 1]

print(statistics.fmean(valores))
print(statistics.fmean(valores_int))

# statistics.geometric_mean - calcula a média geométrica de numeros reais
print(statistics.geometric_mean(valores))
print(statistics.geometric_mean(valores_int))

# statistics.multimode - retorna o valor mais frequente em uma sequencia
seq1 = 'Lala jen fjakf skjff'
seq2 = [2, 4, 5, 32, 4, 3, 5, 2, 4]
seq3 = [1, 1, 2, 2, 3, 3, 4]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
