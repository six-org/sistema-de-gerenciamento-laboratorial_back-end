from django.contrib.auth import get_user_model
import uuid
from django.db import models

User = get_user_model()

class Paciente(models.Model):
    TIPO_SANGUINEO_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField()
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    nome_pai = models.CharField(max_length=255, blank=True, null=True)
    nome_mae = models.CharField(max_length=255, blank=True, null=True)
    tipo_sanguineo = models.CharField(max_length=3, choices=TIPO_SANGUINEO_CHOICES)
    alergias = models.TextField(blank=True)
    comorbidades = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

def __str__(self):
    return self.nome_completo if self.nome_completo else "Paciente sem nome"
