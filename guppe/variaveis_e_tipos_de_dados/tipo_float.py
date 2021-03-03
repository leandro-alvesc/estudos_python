"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais são . e não ,
"""
# Errado do ponto de vista do Float, mas gera uma Tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1.44, 44.1
print(valor1)
print(valor2)

# Podemos converter um float para um int
# OBS: Ao converter um valor float para inteiro, perdemos precisão
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(variavel)
print(type(variavel))
