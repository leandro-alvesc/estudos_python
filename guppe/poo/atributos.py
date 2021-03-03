"""
POO - Atributos

Representam as características do objeto. Ou seja, pelos atributos conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de Instância: Atributos declarados dentro do método construtor.

Em Python, por convenção, ficou estabelecido que t0do atributo de uma classe é público
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, utiliza-se __ duplo underscore.
Isso também é conhecido como Name Mangling.
"""


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class Acesso:
    def __init__(self, email, senha):
        self.email = email  # private = __
        self.__senha = senha

    def mostra_senha(self):
        return self.__senha

# OBS: __ é apenas uma convenção. A linguagem Python não vai impedir que façamos acesso aos atributos sinalizados como
# privados fora da classe


"""
# Atributos de Instância
# O que significa atributos de instancia? Ao criarmos instâncias/objetos de uma classe, todas as instâncias terão esses
# atributos

user = Acesso('user@user.com', '123456')

print(user.email)

print(user.__senha)  # Attribute Error

print(user._Acesso__senha)  # Não vai dar erro, mas sim uma atenção de que isso não deveria ser feito (Name Mangling)

print(user.mostra_senha())
"""

"""
# Atributos de Classe
São atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos
um valor, e esse valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância
da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas
as instâncias terão o mesmo valor para esse atributo.

OBS: Em linguagens como Java, são conhecidos como atributos estáticos.

p1 = Produto('Mesa de Jantar', 'Mesa para sala de jantar', 500)
p2 = Produto('Mesa de Escritório', 'Mesa para escritório', 500)

print(p1.valor)
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto)
print(Produto.contador)
"""


class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        # self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        # Produto.contador = self.id
        Produto.contador += 1


"""
# Atributos Dinâmicos
Um atributo de instância que pode ser criado em tempo de execução.

OBS: O atributo dinâmico será exclusivo da instância que o criou.
"""
p1 = Produto('Mesa de Jantar', 'Mesa para sala de jantar', 500)
p2 = Produto('Mesa de Escritório', 'Mesa para escritório', 500)

# Criando um atributo dinâmico em tempo de execução
p1.peso = '20Kg'  # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p1.nome} \n'
      f'Descrição: {p1.descricao} \n'
      f'Valor: {p1.valor} \n'
      f'Peso: {p1.peso} \n')

print(f'Produto: {p2.nome} \n'
      f'Descrição: {p2.descricao} \n'
      f'Valor: {p2.valor} \n'
      # f'Peso: {p2.peso} \n') # Erro
      )

# Deletando Atributos
print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)
del p1.peso
del p1.descricao

print(p1.__dict__)
print(p2.__dict__)
