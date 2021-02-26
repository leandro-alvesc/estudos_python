"""
Decoradores (Decorators)
- São funções
- Envolvem outras funções e aprimoram seus comportamentos
- Também são exemplos de Higher Order Functions
- Tem uma sintaxe própria, usando "@" (Syntactic Sugar)
- Não confundir Decorator (@decorator) com Decorator Function(função decoradora)


# Decorator como funções (Sintaxe não recomendada - Sem Syntactic Sugar)


def cumprimento(funcao):
    def ola():
        print('---------------')
        funcao()
        print('Seja bem vindo.')
        print('---------------')
    return ola


def salve():
    print('Salve!')


# Testando
teste = cumprimento(salve)

teste()

"""
# Decorator com Syntactic Sugar


def cumprimento(funcao):
    def ola():
        print('---------------')
        funcao()
        print('Seja bem vindo.')
        print('---------------')
    return ola


@cumprimento
def salve():
    print('Salve!')


# Testando
salve()


@cumprimento
def bom_dia():
    print('Bom dia!')


bom_dia()
