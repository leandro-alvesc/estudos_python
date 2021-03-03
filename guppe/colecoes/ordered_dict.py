"""
Módulo Collections: Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

OrderedDict -> É um dicionário que garante a ordem de inserção dos elementos.

# Importando
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(dicionario)
"""
# Entendendo a diferença
from collections import OrderedDict
# Dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True, já que a ordem dos elementos no dicionário comum não importa

# Ordered Dict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False, já que a ordem dos elementos importam para o OrderedDict
