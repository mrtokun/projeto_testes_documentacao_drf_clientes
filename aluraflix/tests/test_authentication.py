from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """ Teste que verifica a autenticação de um user com as credenciais corretas"""
        # O metodo abaixo authenticate não pode ser usado para fazer outras solicitacoes, serve apenas para testar o mecanismo de autenticacao
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and (user.is_authenticated)) 

    def test_requisicao_get_nao_autorizada(self):
        """ Teste que verifica uma requisicao GET nao autorizada"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_do_user_com_username_incorreto(self):
        """ Teste que verifica se o módulo de autenticacao está verificando um user existente"""
        user = authenticate(username='xpto', password='789789')
        self.assertFalse((user is not None) and (user.is_authenticated)) 

    def test_autenticacao_do_user_com_password_incorreto(self):
        """ Teste que verifica se o módulo de autenticacao está verificando a senha correta"""
        user = authenticate(username='c3po', password='789789')
        self.assertFalse((user is not None) and (user.is_authenticated)) 

    def test_requisicao_get_com_user_autenticado(self):
        """ Teste que verifica uma requisicao GEt com um user autenticado"""
        # O metodo abaixo force_authenticate é usado quando preciso manter a conexao para realizar outros testes.
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

