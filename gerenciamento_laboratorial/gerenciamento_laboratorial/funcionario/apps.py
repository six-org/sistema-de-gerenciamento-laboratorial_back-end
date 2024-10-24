from django.apps import AppConfig


class FuncionarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gerenciamento_laboratorial.funcionario'

    verbose_name = 'funcionario'
