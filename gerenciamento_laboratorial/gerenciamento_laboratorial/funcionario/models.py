import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Funcionario(models.Model):
    """ Modelo de Funcionário """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("usuário"))
    cargo = models.CharField(_("Cargo"), max_length=50, blank=True)

    def __str__(self):
        """ Retorna uma string que representa o objeto """
        return str(self.user.name)
