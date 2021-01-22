"""
Set Comprehension

lista = [1, 2, 3, 4, 5, 6]
set = {1, 2, 3, 4, 5, 6}
"""
# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# Outro Exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# OBS: Para virar um dicionário:
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para finalizar
letras = {letra for letra in 'Kendrick Lamar'}
print(letras)
