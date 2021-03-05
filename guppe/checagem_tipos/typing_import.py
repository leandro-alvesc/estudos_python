"""
nomes: list = ['Teste', 'Teste2']

versoes: tuple = (3, 2, 1)

op_dict: dict = {'um': 1, 'dois': 2}

valor: set = {1, 3, 5}

print(nomes)
print(versoes)
print(op_dict)
print(valor)
print(__annotations__)
"""
from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Teste', 'Teste2']

versoes: Tuple[int, int, str] = (3, 1, '2')

op_dict: Dict[str, int] = {'um': 1, 'dois': 2}

valor: Set[int] = {1, 3, 5}

print(nomes)
print(versoes)
print(op_dict)
print(valor)
print(__annotations__)
