"""
POO - Herança Múltipla

É a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde
todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta
    - Por Multiderivação Indireta

# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta


class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):
    pass


class Multiderivada2(Base6):
    pass


# OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos e
métodos das super classes.
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Mamifero(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def correr(self):
        return f'{self.nome} está correndo.'


class Gato(Mamifero):

    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        return f'{self.nome} está miando.'


class SuperAnimal:
    @staticmethod
    def voar():
        return 'Está voando'


class SuperGato(Gato, SuperAnimal):  # Se tiver dois métodos de nomes iguais, ele executa o primeiro da herança (MRO)
    def voar(self):
        return f'{self.nome} está voando!'


g = SuperGato('Garfield')

print(g.miar())
print(g.correr())
print(g.voar())

print(f'{g.nome} é intância de Gato? {isinstance(g, Gato)}')
print(f'{g.nome} é intância de Animal? {isinstance(g, Animal)}')
print(f'{g.nome} é intância de Mamífero? {isinstance(g, Mamifero)}')
print(f'{g.nome} é intância de object? {isinstance(g, object)}')
