"""
POO - Propriedades (Properties)

Em linguagens de programação como Java, ao declararmos atributos privados nas classes, costumamos
criar métodos públicos para a manipulação desses atributos. Esses métodos são conhecidos como
getters e setters.

class Lampada:
    def __init__(self, cor, watts, luminosidade):
        self.__cor = cor
        self.__watts = watts
        self.__luminosidade = luminosidade
        self.__ligada = False

    def get_cor(self):
        return self.__cor

    def get_watts(self):
        return self.__watts

    def get_luminosidade(self):
        return self.__luminosidade

    def set_cor(self, cor):
        self.__cor = cor

    def set_watts(self, watts):
        self.__watts = watts

    def set_luminosidade(self, luminosidade):
        self.__luminosidade = luminosidade

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


l1 = Lampada('Amarelo', 5, 1500)

print(l1.get_cor())
l1.set_luminosidade(1200)
print(l1.get_luminosidade())
"""


class Lampada:
    def __init__(self, cor, watts, luminosidade):
        self.__cor = cor
        self.__watts = watts
        self.__luminosidade = luminosidade
        self.__ligada = False

    @property
    def cor(self):
        return self.__cor

    @property
    def watts(self):
        return self.__watts

    @property
    def luminosidade(self):
        return self.__luminosidade

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @watts.setter
    def watts(self, watts):
        self.__watts = watts

    @luminosidade.setter
    def luminosidade(self, luminosidade):
        self.__luminosidade = luminosidade

    @property  # utilizando métodos como propriedades
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


l1 = Lampada('Amarelo', 5, 1500)

print(l1.cor)
print(l1.luminosidade)
l1.luminosidade = 1200
print(l1.luminosidade)
print(l1.descricao)
