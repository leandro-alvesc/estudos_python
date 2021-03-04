"""
POO - MRO (Method Resolution Order)

É a ordem de execução dos métodos: quem será executado primeiro.

Em Python podemos conferir a ordem de execução de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help
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

    def correr(self):
        return f'{self.nome} está correndo.'


class SuperAnimal:
    @staticmethod
    def voar():
        return 'Está voando'

    @staticmethod
    def correr():
        return 'Está correndo muito rápido!'


class SuperGato(SuperAnimal, Gato):  # Se tiver dois métodos de nomes iguais, ele executa o primeiro da herança (MRO)
    def voar(self):
        return f'{self.nome} está voando!'


g = SuperGato('Garfield')

print(g.miar())
print(g.correr())
print(g.voar())

# MRO
print(SuperGato.__mro__)
print(SuperGato.mro())
print(help(SuperGato))
