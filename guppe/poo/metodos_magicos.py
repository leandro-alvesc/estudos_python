"""
POO - Métodos Mágicos

São os métodos que utilizam dunder.

Dunder -> Double Underscore

dunder init -> __init__()
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    # dunder repr -> Representação do objeto
    def __repr__(self):
        return f'{self.__titulo} por {self.__autor}'

    # dunder str -> Tem preferência em relação ao repr na função print()
    def __str__(self):
        return f'{self.__titulo} por {self.__autor} com {self.__paginas} páginas'

    # dunder len -> Função len() para o objeto
    def __len__(self):
        return self.__paginas

    # dunder del -> mudar o comportamento do del (sempre é executado ao final do programa)
    def __del__(self):
        print(f'O objeto Livro ({self.__titulo}) foi deletado')

    # dunder add
    def __add__(self, other):
        return f'{self} - {other}'

    # dunder mul
    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += str(self) + ' '
            return msg
        return 'Impossível multiplicar'


livro1 = Livro('Estrada da Noite', 'Joe Hill', 250)
livro2 = Livro('It', 'Stephen King', 1000)

print(livro1)
print(livro2)
print(len(livro1))
print(len(livro2))
print(livro1 + livro2)
print(livro1 * 3)
