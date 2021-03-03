"""
Escrevendo um iterador customizado


# Iterando
con = Contador(1, 5)

it = iter(con)

print(next(con))
print(next(con))
print(next(con))
print(next(con))
"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


for n in Contador(2, 15):
    print(n)

for n in range(2, 15):
    print(n)
