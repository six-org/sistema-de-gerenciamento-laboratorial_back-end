from rest_framework import serializers
from gerenciamento_laboratorial.exame.models import Exame


class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = ('id', 'tipo', 'data_hora', 'descricao',
                  'resultado', 'paciente', 'valor')
        read_only = ('id',)
