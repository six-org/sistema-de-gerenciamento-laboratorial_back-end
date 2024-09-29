import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.core.validators import MinLengthValidator
from .validators import valid_cpf_validator, maior_de_idade_validator


class User(AbstractUser):
    """
    Custom user model for GerenciamentoLaboratorial.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None
    last_name = None
    nivel_acesso = models.CharField(
        _("Nível de Acesso"), max_length=50, blank=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, validators=[
                           MinLengthValidator(11), valid_cpf_validator])

    def get_absolute_url(self) -> str:
        """ Retorna a URL do detalhe do usuário. """
        return reverse("users:detail", kwargs={"username": self.username})


class Funcionario(models.Model):
    """ Modelo de Funcionário """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("usuário"))
    data_nascimento = models.DateField(
        _("Data de Nascimento"), blank=True, null=True,
        validators=[maior_de_idade_validator])
    cargo = models.CharField(_("Cargo"), max_length=50, blank=True)

    def __str__(self):
        """ Retorna uma string que representa o objeto """
        return str(self.user.name)
