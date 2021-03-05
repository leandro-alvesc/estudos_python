from typing import Literal, Union, Final, final, TypedDict, Protocol
# int str float List Set Dict etc

"""
def dobro(valor: int) -> int:
    return valor * 2


print(dobro(7))
print(dobro('rs'))  # Ferramentas como mypy apresentaria o erro
"""
"""
- Literal type
- Union
- Final
- Typed dictionaries
- Protocols
"""
# Literal Type


def calcula(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula('+', 1, 2)
calcula('-', 3, 1)
"""
calcula('*', 4, 3) 

no mypy ele apresenta tipos_de_dados_mais_precisos.py:33: error: Argument 1 to "calcula" has incompatible type 
"Literal['*']"; expected "Union[Literal['+'], Literal['-']]"
"""


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado


NOME: Final = 'José'

print(NOME)

# NOME = 'Teste'  # Problema com mypy

print(NOME)

"""
@final
class Pessoa:
    pass


class Estudante(Pessoa):  # mypy erro

    @final
    def estudar(self):
        print('Estou estudando')


class Estagiario(Estudante):

    def estudar(self):
        print('Teste')
"""


class CursoPython(TypedDict):
    versao: str
    att: int


lala = CursoPython(versao='3.1.2', att=2021)

print(lala)


# Protocols
class Curso(Protocol):
    titulo: str


class CursoUm(Curso):

    def __init__(self, titulo):
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


teste = CursoUm('Python')
estudar(teste)
