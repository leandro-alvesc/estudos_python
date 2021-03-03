"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

# Exemplo all()
print(all([0, 1, 2, 3]))  # False
print(all([1, 2, 3]))  # True
print(all([]))  # True
print(all((1, 2, 3)))  # True
print(all({1, 2, 3}))  # True
print(all(['Jose']))  # True

nomes = ['Carlos', 'Camila', 'Cléber', 'Cristiano', 'Catarina']

print(all([nome[0] == 'C' for nome in nomes]))


any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""
print(any([0, 1, 2, 3]))  # True
print(any([0, False, {}, (), []]))  # False

nomes = ['Carlos', 'Camila', 'Cléber', 'Cristiano', 'Catarina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))  # True
