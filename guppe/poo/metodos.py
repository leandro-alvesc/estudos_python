"""
POO - Métodos

- Métodos(funções) -> Representam os comportamentos do objeto. Ou seja, a ação que pode ser realizada.

Em Python, dividimos em 2 grupos:
    - Métodos de Instância
    - Métodos de Classe

"""
# Métodos de Instância
# O método dunder init (__init__) é o método construtor.
# Os métodos dunder em Python são chamados de métodos mágicos
# Atenção: Não é recomendado criar funções dunder.
# Métodos são escritos em letras minúsculas, caso seja composto será separada por underline


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


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


"""
p1 = Produto('Nintendo Switch', 'Console', 3000)

print(p1.desconto(10))

# print(Produto.desconto(p1, 10))  # self, desconto

l1 = Lampada('Amarela', 15, 1500)

print(l1.ligar())
print(l1.ligar())
print(l1.desligar())
print(l1.descricao())
"""
from passlib.hash import pbkdf2_sha256 as crypt


class User:

    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = User.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crypt.hash(senha, rounds=200000, salt_size=16)
        User.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def autenticar(self, senha):
        if crypt.verify(senha, self.__senha):
            return True
        return False

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    # Métodos Privados - Por convenção utiliza-se __
    def __gera_usuario(self):
        return self.__email.split('@')[0]

    # Sem cls nem self
    @staticmethod
    def teste():
        return 'teste'


"""
nome_user = input('Nome: ')
sobrenome_user = input('Sobrenome: ')
email_user = input('Email: ')
senha_user = input('Senha: ')
confirma_senha_user = input('Confirme a senha: ')

if senha_user == confirma_senha_user:
    user1 = User(nome_user, sobrenome_user, email_user, senha_user)
else:
    print('Senha não confere')
    exit(1)

    print('Usuário criado com sucesso!')
senha = input('Informe a senha: ')

if user1.autenticar(senha):
    print('Acesso concebido')
else:
    print('Acesso negado')

# print(f'Senha criptografada: {user1._User__senha}')  # acesso não recomendado
"""
# Métodos de Classe - Conhecidos como métodos estáticos
user1 = User('João', 'Carlos', 'joao@user.com', '123456')

User.conta_usuarios()  # Forma correta
# user1.conta_usuarios()  # Possível, porém incorreto
print(User.teste())
