from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'email', 'data_nascimento', 'tipo_sanguineo')
    search_fields = ('nome_completo', 'cpf')
    fields = ('nome_completo', 'cpf', 'data_nascimento', 'email', 'rua', 'bairro', 'cidade', 'cep', 'nome_pai', 'nome_mae', 'tipo_sanguineo', 'alergias', 'comorbidades', 'user')

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user  # Atribui o usuário logado como o `user`
        super().save_model(request, obj, form, change)
