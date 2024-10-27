from rest_framework import serializers
from gerenciamento_laboratorial.exame.models import Exame
from gerenciamento_laboratorial.atendimento.models import Atendimento


class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = ('id', 'tipo', 'data_hora', 'descricao',
                  'resultado', 'paciente', 'valor')
        read_only = ('id',)

    def validate_data_hora(self, value):

        if not Atendimento.objects.filter(horario_atendimento=value).exists():
            raise serializers.ValidationError(
                'Data de atendimento não encontrada')

        atendimento = Atendimento.objects.filter(
            horario_atendimento=value).first()
        quantidade_exames_macados = Exame.objects.filter(
            data_hora=value).count()

        if quantidade_exames_macados >= atendimento.limite_fichas:
            raise serializers.ValidationError(
                'Quantidade máxima de exames para esta data de atendimento alcançada.')

        return value
