"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:
# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0 com passo 1)

for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado com passo 1)

for num in range(4, 15):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado com passo especificado)

for num in range(5, 50, 5):
    print(num)

# Forma 4 (inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado com passo especificado)

for num in range(10, 0, -1):
    print(num)


"""

