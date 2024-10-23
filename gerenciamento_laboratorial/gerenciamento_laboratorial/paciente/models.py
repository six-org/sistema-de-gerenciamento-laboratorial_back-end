import uuid
from django.db import models
from django.utils.text import gettext_lazy as _
from django.contrib.auth import get_user_model
from .validators import text_regex_validator


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
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("usuário"))
    tipo_sanguineo = models.CharField(
        max_length=3, choices=TIPO_SANGUINEO_CHOICES)
    alergias = models.TextField(blank=True, validators=[text_regex_validator])
    comorbidades = models.TextField(
        blank=True, validators=[text_regex_validator])

    def _str_(self):
        return self.nome
