from django.contrib import admin
from gerenciamento_laboratorial.funcionario.models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'cpf', 'data_nascimento', 'nivel_acesso']
    search_fields = ['nome_completo', 'cpf']
