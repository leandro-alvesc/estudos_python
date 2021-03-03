"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> Agrupamento de atributos e métodos. Exemplo: a classe pode encapsular nossos métodos e atributos

Os atributos não ficam de fácil acesso.
Lembrando que o Python não bloqueia o acesso, mas sim cria o Name Mangling

Abstração em POO é o ato de expor apenas dados relevantes de uma classe. escondendo atributos e métodos privados do
usuário.

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


lampada1 = Lampada('Amarela', 5, 1500)

# lampada1.__ligada = True  # Forma errada (Assim irá criar um novo atributo de nome __ligada pois com o Name Mangling
# o atributo se chama _Lampada__ligada)
print(lampada1.ligar())
print(lampada1.desligar())
