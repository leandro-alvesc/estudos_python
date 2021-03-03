"""
POO - super()

O método super() se refere à super classe
"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, especie, pelo):
        Animal.__init__(self, nome, especie)
        # super().__init__(nome, especie)
        self.__pelo = pelo


garfield = Gato('Garfield', 'Felino', 'Grande')

garfield.faz_som('miau')
