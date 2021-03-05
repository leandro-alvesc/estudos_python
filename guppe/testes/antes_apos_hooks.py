"""
Unittest - Antes e após hooks

hooks são os testes em si, ou seja, a execução dos testes

setUp() -> executado antes de cada método de teste, é útil para criarmos instâncias de objetos e outros dados

tearDown() -> é executado ao final de cada método de teste, é útil para excluir dados ou fechar conexões com DB
"""
import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai executar antes do teste
        # tearDown vai executar aoós o teste
        pass

    def test_segundo(self):
        # setUp vai executar antes do teste
        # tearDown vai executar aoós o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
