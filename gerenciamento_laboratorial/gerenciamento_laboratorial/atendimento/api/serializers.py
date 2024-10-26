from rest_framework import serializers
from ..models import Atendimento


class AtendimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atendimento
        fields = ("id", "horario_atendimento", "limite_fichas")
