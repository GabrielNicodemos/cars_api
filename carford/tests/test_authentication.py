from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status



class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )

        self.url = reverse('owners-list')

    def test_auth_user_correct_credentials(self):
        """Teste que verifica credenciais corretas de um usuário"""
        userAuthenticate = authenticate(username='admin', password='admin')
        self.assertTrue((userAuthenticate is not None) and (userAuthenticate.is_authenticated))

    def test_auth_user_incorrect_username(self):
        """Teste que verifica credenciais incorretas de um usuário com username incorreta"""

        userAuthenticate = authenticate(username='admin1', password='admin')
        self.assertFalse((userAuthenticate is not None) and (userAuthenticate.is_authenticated))

    def test_auth_user_incorrect_password(self):
        """Teste que verifica credenciais incorretas de um usuário com senha incorreta"""

        userAuthenticate = authenticate(username='admin', password='admin1')
        self.assertFalse((userAuthenticate is not None) and (userAuthenticate.is_authenticated))

    def test_request_get_auth(self):
        """Teste que verifica requisição GET autorizada"""

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_not_auth(self):
        """Teste que verifica requisição GET autorizada"""

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)