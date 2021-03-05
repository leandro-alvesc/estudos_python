import unittest

from atividades import comer, dormir, engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_suadavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_nao_saudavel(self):
        """Testando o retorno com comida não saudável"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque YOLO'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Dormi por apenas 4 horas. Tenho que melhorar meu sono!'
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Dormi 10 horas! Estou atrasado...'
        )

    def test_dormir_bem(self):
        """Testando o retorno dormindo bem"""
        self.assertEqual(
            dormir(8),
            'Dormi por 8 horas, estou descansado!'
        )

    def test_engracada(self):
        # self.assertEqual(engracada('Danola Gentolla'), False)
        self.assertFalse(engracada('Danola Gentolla'))
        self.assertTrue(engracada('Jim Carrey'), 'Jim Carrey é engraçado.')


if __name__ == '__main__':
    unittest.main()

