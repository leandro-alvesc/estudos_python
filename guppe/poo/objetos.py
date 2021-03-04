"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento devemos poder criar quantos objetos forem
necessários. Como se fosse variáveis do tipo da classe.

T0do objeto herda da classe objects.
"""


class Lampada:
    def __init__(self, cor, watts, luminosidade):
        self.__cor = cor
        self.__watts = watts
        self.__luminosidade = luminosidade
        self.__ligada = False

    def descricao(self):
        return f'Cor: {self.__cor}\nWatts: {self.__watts}W \nLuminosidade: {self.__luminosidade} Lumens'

    def ligar(self):
        if not self.__ligada:
            self.__ligada = True
            return 'Ligou'
        return 'Já está ligada'

    def desligar(self):
        if self.__ligada:
            self.__ligada = False
            return 'Desligou'
        return 'Já está desligada'


lampada1 = Lampada('Amarela', 5, 1500)  # <- Objeto
