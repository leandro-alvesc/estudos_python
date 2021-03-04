"""
POO - Polimorfismo

Objetos que podem possuir muitas formas
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar o método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala au au!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala miau!')


gato = Gato('Garfield')
gato.comer()
gato.falar()

cachorro = Cachorro('Pateta')
cachorro.comer()
cachorro.falar()


