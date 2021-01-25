"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.4'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.4"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a'''', '''True''', '''42.4'''
"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.4"""

# nome = """Leandro"""
# print(nome)
# print(type(nome))
"""
nome = 'Leandro'
print(nome)
print(type(nome))

nome = "Leandro's Bar"
print(nome)
print(type(nome))

nome = 'Leandro \nAlves'
print(nome)
print(type(nome))
"""
# nome = """Leandro
# Alves"""
# print(nome)
# print(type(nome))
"""
nome = "Leandro \" Alves"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome.strip()) # Tira os espaços desnecessários de uma string
"""
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12 ]
# ['L', 'e', 'a', 'n', 'd', 'r', 'o', ' ', 'A', 'l', 'v', 'e', 's']
nome = 'Leandro Alves'
print(nome[0:7]) # Slice de String
print(nome[8:13])

print(nome.split())
print(nome.split()[0])

# [::-1] -> Comece do primeiro elemento, vá até o último e inverta
print(nome[::-1]) # Inversão da String Pythônico

print(nome.replace('L', 'K'))

