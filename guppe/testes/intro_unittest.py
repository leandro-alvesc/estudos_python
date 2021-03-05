"""
Introdução ao módulo Unittest

Testes unitários -> é a foma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

# OBS: Teste unitário não é específicio da linguagem Python.

Para criar nossos testes criamos classes que herdam de unittest.TestCase e a partir de então
ganhamso todos os assertions presentes do módulo.

Para rodar os testes utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

# Assertions
Método                                  Checa se
assertEqual(a, b)                       a == b
assertNotEqual(a, b)                    a != b
assertTrue(x)                           x é verdadeiro
assertFalse(x)                          x é falso
assertIs(a, b)                          a é b
assertIsNot(a, b)                       a não é b
assertIfNone(x)                         x é None
assertIsNotNone(x)                      x não é None
assertIn(a, b)                          a está em b
assertNotIn(a, b)                       a não está em b
assertIsInstance(a, b)                  a é instância de b
assertNotIsInstance(a, b)               a não é instância de b


Por convenção, todos os testes em um testcase devem ter seu nome iniciado com test_

Para executar os testes com unittest:
    python nome_do_arquivo.py

Para executar os testes com unittest no modo verbose
    python nome_do_arquivo.py -v

Docstrings nos testes
- Podemos acrescentar e é recomendado acrescentar Docstrings nos testes
"""
# Prática - TDD
