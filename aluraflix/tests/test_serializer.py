from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'A batalha final',
            data_lancamento = '2003-07-04',
            tipo='F',
            likes = 1844,
            dislikes = 44
        )
        self.serializer = ProgramaSerializer(instance = self.programa)
    
    def test_verifica_campos_serializados(self):
        """ Teste que verifica os campos que estão sendo serializados"""
        dados = self.serializer.data
        self.assertEqual(set(dados.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    # def test_verifica_campos_serializados_que_falha(self):
    #     """ Teste que falha verifica se na ausência de um dos campos que estão sendo serializados dá erro"""
    #     dados = self.serializer.data
    #     self.assertSetEqual(set(dados.keys()), set(['titulo', 'tipo', 'data_lancamento']))
    
    def test_verifica_conteudo_campos_serializados(self):
        """ Teste que verifica o conteudo dos campos serializados"""
        dados = self.serializer.data
        self.assertEqual(dados['titulo'], self.programa.titulo)
        self.assertEqual(dados['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(dados['tipo'], self.programa.tipo)
        self.assertEqual(dados['likes'], self.programa.likes)
        