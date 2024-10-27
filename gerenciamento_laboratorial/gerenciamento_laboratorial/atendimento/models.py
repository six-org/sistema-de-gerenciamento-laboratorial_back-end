import uuid
from django.db import models


class Atendimento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    horario_atendimento = models.DateTimeField(
        verbose_name="Horário do atendimento")
    limite_fichas = models.PositiveIntegerField(
        verbose_name="Limite de fichas disponíveis")

    def __str__(self):
        return f"Atendimento em {self.horario_atendimento} - fichas disponíveis: {self.limite_fichas}"
