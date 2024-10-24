from rest_framework import serializers
from gerenciamento_laboratorial.paciente.models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            'id', 'nome_completo', 'cpf', 'data_nascimento', 'email', 
            'rua', 'bairro', 'cidade', 'cep', 'nome_pai', 'nome_mae', 
            'tipo_sanguineo', 'alergias', 'comorbidades'
        ]
