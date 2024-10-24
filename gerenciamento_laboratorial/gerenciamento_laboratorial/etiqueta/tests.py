from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from gerenciamento_laboratorial.users.models import User
from gerenciamento_laboratorial.etiqueta.models import Etiqueta
import uuid

from rest_framework_simplejwt.tokens import RefreshToken

class EtiquetaModelViewSetTestCase(APITestCase):
    def setUp(self):
        # Cria um usuário comum e um admin
        self.user = User.objects.create_user(username="user", password="password")
        self.admin = User.objects.create_superuser(username="admin", password="password")

        # Cria uma etiqueta de teste
        self.etiqueta = Etiqueta.objects.create(
            codigo="COD123",
            tipo_exame="Exame de Sangue",
            data_coleta="2024-10-21",
            hora_coleta="10:30"
        )

        # Cliente para simular requisições
        self.client = APIClient()

    def authenticate(self, user):
        """Função para autenticar o usuário e adicionar o token JWT ao header"""
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_list_etiqueta_as_non_admin(self):
        # Autentica o usuário comum
        self.authenticate(self.user)
        url = reverse('api:etiqueta-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_etiqueta_as_admin(self):
        # Autentica o usuário admin
        self.authenticate(self.admin)
        url = reverse('api:etiqueta-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_etiqueta_as_non_admin(self):
        # Autentica o usuário comum
        self.authenticate(self.user)
        url = reverse('api:etiqueta-detail', args=[self.etiqueta.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['codigo'], 'COD123')

    def test_retrieve_etiqueta_as_admin(self):
        # Autentica o usuário admin
        self.authenticate(self.admin)
        url = reverse('api:etiqueta-detail', args=[self.etiqueta.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_etiqueta_as_non_admin(self):
        # Autentica o usuário comum
        self.authenticate(self.user)
        url = reverse('api:etiqueta-list')
        data = {
            "codigo": "COD789",
            "tipo_exame": "Exame de Sangue",
            "data_coleta": "2024-10-21",
            "hora_coleta": "11:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_etiqueta_as_admin(self):
        # Autentica o usuário admin
        self.authenticate(self.admin)
        url = reverse('api:etiqueta-list')
        data = {
            "codigo": "COD456",
            "tipo_exame": "Exame de Urina",
            "data_coleta": "2024-10-21",
            "hora_coleta": "09:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_etiqueta_as_admin(self):
        # Autentica o usuário admin
        self.authenticate(self.admin)
        url = reverse('api:etiqueta-detail', args=[self.etiqueta.id])
        data = {
            "codigo": "COD321",
            "tipo_exame": "Exame de Sangue",
            "data_coleta": "2024-10-21",
            "hora_coleta": "10:30"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.etiqueta.refresh_from_db()
        self.assertEqual(self.etiqueta.codigo, "COD321")

    def test_delete_etiqueta_as_non_admin(self):
        # Autentica o usuário comum
        self.authenticate(self.user)
        url = reverse('api:etiqueta-detail', args=[self.etiqueta.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_etiqueta_as_admin(self):
        # Autentica o usuário admin
        self.authenticate(self.admin)
        url = reverse('api:etiqueta-detail', args=[self.etiqueta.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Etiqueta.objects.count(), 0)
