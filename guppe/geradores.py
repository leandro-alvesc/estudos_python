"""
Geradores
- Geradores (Generators) são Iteradores (Iterators)
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com Expressões Geradoras;
    - Diferenças entre Funções e Generator Functions
        --------------------------------------------------------------
        |        Funções          |      Generators Functions        |
        --------------------------------------------------------------
        | utilizam return         | utilizam yield                   |
        --------------------------------------------------------------
        | retorna uma vez         | podem usar yield multiplas vezes |
        --------------------------------------------------------------
        | retorna um valor        | retorna um generator             |
        --------------------------------------------------------------



gen = conte_ate(5)

# print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for n in gen:
    print(n)

gen = conte_ate(10)

next(gen)

for n in gen:  # Começará do 2 já que utilizou o next acima
    print(n)

"""
# Exemplo de Generator Function


def conte_ate(maximo):
    contador = 1
    while contador <= maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator, ela gera um Generator


gen = list(conte_ate(10))
print(gen)
