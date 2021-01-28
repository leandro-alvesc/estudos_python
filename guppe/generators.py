"""
Generators - Generator Expression
Em aulas anteriores vimos:
    - List Comprehension;
    - Dicionary Comprehension;
    - Set Comprehension.

- Tuple Comprehension se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Carminda', 'Gustavo']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
"""
# getsizeof() -> Retorna a quantidade de bytes em memória de um elemento passado como parâmetro
from sys import getsizeof

# print(getsizeof('Carlos'))
# print(getsizeof('Jubileu Armando'))
# print(getsizeof(7))
# print(getsizeof(68))
# print(getsizeof(8491230))
# print(getsizeof(True))

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# lista com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa, memória usada: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')
print(f'Generator Expression: {getsizeof(tuple(x * 10 for x in range(1000)))} bytes')

"""
# Iterar em um Generator
gen2 = (x * 10 for x in range(1000))
for num in gen2:
    print(num)
"""

