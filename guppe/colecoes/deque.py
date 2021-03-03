"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.


"""
# Importação
from collections import deque

# Criando deques
deq = deque('teste')
print(deq)

# Adicionando elementos no deque
deq.append('b')  # Adiciona no final
print(deq)

deq.appendleft('a')  # Adiciona no começo da lista
print(deq)

# Remover elementos
print(deq.pop())  # Remove e retorna o último elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)
