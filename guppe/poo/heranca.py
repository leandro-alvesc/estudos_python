"""
POO - Herança (Inheritance)

A ideia de Herança é de reaproveitar o código e também estender nossas classes.

OBS: Quando uma classe herda outra classe, ela herda todos os atributos e métodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada (Pessoa) é conhecida por:
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica

Quando uma classe herda de outra classe, ela (Cliente, Funcionario) é chamada:
    - Sub Classe
    - Classe Filha
    - Classe Específica
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'Nome: {self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Sobrescrever métodos (Overriding)
    def nome_completo(self):
        return f'Funcionário: {self.__matricula}\n{super().nome_completo()}'


cliente1 = Cliente('Joao', 'Roberto', '123.456.789-88', 5000)
funcionario1 = Funcionario('Maria', 'Joana', '789.456.123-00', 1234)

print(cliente1.nome_completo())
print()
print(funcionario1.nome_completo())
