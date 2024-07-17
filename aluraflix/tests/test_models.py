from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando nemo',
            data_lancamento = '2003-07-04'
        )

    def test_verifica_atributos_default(self):
        """ Teste que verifica a criação de um Programa e atribuição de valores default"""
        self.assertEqual(self.programa.titulo, 'Procurando nemo')
        self.assertEqual(self.programa.data_lancamento, '2003-07-04')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)