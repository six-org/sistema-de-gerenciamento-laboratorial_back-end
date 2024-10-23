import uuid
from django.utils import timezone
from django.db import models
from gerenciamento_laboratorial.paciente.models import Paciente
from .validators import text_regex_validator


class Exame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=50)
    data_hora = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(validators=[text_regex_validator])
    resultado = models.TextField(validators=[text_regex_validator])
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name='exames')
    valor = models.FloatField()

    def _str_(self):
        return f"Exame de {self.tipo} - Paciente: {self.paciente.nome}"
