"""
Preservando Metadatas com Wraps

Metadatas -> Dados intríssecos

Wraps -> Funções que envolvem elementos com diversas finalidades.



# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        """"""Função (logar) dentro de outra""""""
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Documentação: {funcao.__doc__}')
        return funcao(*args, *kwargs)
    return logar


@ver_log
def soma(a, b):
    """"""Soma dois números""""""
    return a + b


# print(soma(10, 20))

print(soma.__name__)  # os metadados estão sendo decorados
print(soma.__doc__)

"""
# Resolução
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Função (logar) dentro de outra"""
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Documentação: {funcao.__doc__}')
        return funcao(*args, *kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# print(soma(10, 20))

print(soma.__name__)  # com a função wraps (decorator) resolve o problema
print(soma.__doc__)
