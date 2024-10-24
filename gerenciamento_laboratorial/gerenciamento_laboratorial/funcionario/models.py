import uuid
from django.db import models
from django.conf import settings  # Use settings para acessar AUTH_USER_MODEL

class Funcionario(models.Model):
    """ Modelo de Funcionário """
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='funcionario')
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True, default='000.000.000-00')
    data_nascimento = models.DateField()
    cargo = models.CharField(max_length=100, null=True, blank=True)
    nivel_acesso = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_completo
