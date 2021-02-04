# Verificar se o numero é positivo ou negativo. Se for positivo retornar 1, negativo -1 e se 0 0.


def positivo(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


print(positivo(5))
print(positivo(-4))
print(positivo(0))
