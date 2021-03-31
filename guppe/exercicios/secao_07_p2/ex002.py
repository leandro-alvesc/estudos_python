# Matriz 5x5 com 1 na diagonal principal e 0 os demais
matriz = []
for n in range(5):
    b = []
    for x in range(5):
        if x == n:
            b.append(1)
        else:
            b.append(0)
    matriz.append(b)


for item in matriz:
    print(item)
