from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):
    """"""
    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        filme = Programa.objects.get(pk=1)
        todos_filmes = Programa.objects.all()
        self.assertEqual(filme.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_filmes), 9)
        