from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from gerenciamento_laboratorial.users.models import User
from gerenciamento_laboratorial.exame.models import Exame
from gerenciamento_laboratorial.paciente.models import Paciente
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class ExameViewSetTestCase(APITestCase):

    def setUp(self):
        # Criação de usuários e pacientes
        self.admin = User.objects.create_superuser(username="admin", password="password")
        self.user = User.objects.create_user(username="user", password="password")
        self.paciente = Paciente.objects.create(user=self.user)

        # Criação de exame para o paciente
        self.exame = Exame.objects.create(
            tipo="Sangue",
            data_hora=timezone.now(),
            descricao="Exame de rotina",
            resultado="Negativo",
            paciente=self.paciente,
            valor=100.0
        )

        self.client = self.client_class()

    def authenticate(self, user):
        """Função para autenticar o usuário e adicionar o token JWT ao header"""
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_list_exames_as_admin(self):
        # Autenticar como admin
        self.authenticate(self.admin)
        url = reverse('api:exame-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Exame.objects.count())

    def test_list_exames_as_non_admin(self):
        # Autenticar como usuário comum
        self.authenticate(self.user)
        url = reverse('api:exame-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se o usuário comum vê apenas seus próprios exames
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['tipo'], 'Sangue')
        self.assertEqual(response.data[0]['paciente'], self.paciente.id)

    def test_retrieve_exame(self):
        # Testa se um usuário pode recuperar os detalhes de um exame
        self.authenticate(self.user)
        url = reverse('api:exame-detail', args=[self.exame.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tipo'], 'Sangue')

    def test_create_exame_as_admin(self):
        # Testa se um admin pode criar um novo exame
        self.authenticate(self.admin)
        url = reverse('api:exame-list')
        data = {
            "tipo": "Urina",
            "data_hora": timezone.now(),
            "descricao": "Exame de urina",
            "resultado": "Negativo",
            "paciente": self.paciente.id,
            "valor": 150.0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Exame.objects.count(), 2)

    def test_create_exame_as_non_admin(self):
        # Testa se um usuário comum pode criar um exame (deve ser proibido)
        self.authenticate(self.user)
        url = reverse('api:exame-list')
        data = {
            "tipo": "Urina",
            "data_hora": timezone.now(),
            "descricao": "Exame de urina",
            "resultado": "Negativo",
            "paciente": self.paciente.id,
            "valor": 150.0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_exame_as_admin(self):
        # Testa se um admin pode atualizar um exame
        self.authenticate(self.admin)
        url = reverse('api:exame-detail', args=[self.exame.id])
        data = {
            "tipo": "Sangue",
            "data_hora": timezone.now(),
            "descricao": "Exame atualizado",
            "resultado": "Positivo",
            "paciente": self.paciente.id,
            "valor": 120.0
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.exame.refresh_from_db()
        self.assertEqual(self.exame.descricao, "Exame atualizado")

    def test_delete_exame_as_admin(self):
        # Testa se um admin pode deletar um exame
        self.authenticate(self.admin)
        url = reverse('api:exame-detail', args=[self.exame.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Exame.objects.count(), 0)

    def test_delete_exame_as_non_admin(self):
        # Testa se um usuário comum é proibido de deletar um exame
        self.authenticate(self.user)
        url = reverse('api:exame-detail', args=[self.exame.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_agendamentos_as_admin(self):
        # Testa se o admin pode listar agendamentos
        self.authenticate(self.admin)
        url = reverse('api:exame-list-agendamentos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se o retorno inclui apenas exames em status de agendamento
        agendamentos = Exame.objects.filter(status='AGENDAMENTO')
        self.assertEqual(len(response.data), agendamentos.count())

    def test_list_cancelamentos_as_admin(self):
        # Testa se o admin pode listar cancelamentos
        self.authenticate(self.admin)
        url = reverse('api:exame-list-cancelamentos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se o retorno inclui apenas exames com solicitação de cancelamento
        cancelamentos = Exame.objects.filter(status='CANCELAMENTO')
        self.assertEqual(len(response.data), cancelamentos.count())
