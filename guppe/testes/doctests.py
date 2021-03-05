"""
Doctestes

São testes que colocamos na docstring das funções/métodos Python

Para rodar um doctest:

python -m doctest -v nome_do_arquivo.py

saída:

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
(guppe) b3lzebuth@b3lzebuthASUS:~/PycharmProjects/estudos_python/guppe/testes$ python -m doctest -v doctests.py
7
Trying:
    soma(1, 2)
Expecting:
    3
ok
Trying:
    soma(4, 6)
Expecting:
    10
ok
1 items had no tests:
    doctests
1 items passed all tests:
   2 tests in doctests.soma
2 tests in 2 items.
2 passed and 0 failed.
Test passed.


"""


def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b


print(soma(3, 4))
