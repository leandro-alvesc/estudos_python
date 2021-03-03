"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio, porém
falar que é um tipo sem tipo é mais apropriado.

OBS: O tipo None é sempre especificado com a primeira letra maiúscula
Certo: None
Errado: none

Quando utilizamos:
    - Podemos utilizar quando queremos criar uma variável e inicializá-la com um tipo sem tipo antes de
    receber um valor final.

OBS: O tipo None em Python é sempre considerado como False
"""
numeros = None
print(numeros)
print(type(numeros))

if None:
    print('Sim')
else:
    print('Não')
