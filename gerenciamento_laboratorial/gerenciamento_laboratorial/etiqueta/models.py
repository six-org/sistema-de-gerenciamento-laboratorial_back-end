import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Etiqueta(models.Model):
    """ Modelo de Etiqueta """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(_("Código"), max_length=50, blank=True)
    tipo_exame = models.CharField(
        _("Tipo de Exame"), max_length=50, blank=True)
    data_coleta = models.DateField(_("Data da Coleta"), blank=True, null=True)
    hora_coleta = models.CharField(
        _("Horário da Coleta"), max_length=50, blank=True)

    def __str__(self):
        """ Retorna uma string que representa o objeto """
        return str(self.codigo)
