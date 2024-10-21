from rest_framework import serializers
from ..models import Etiqueta

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = (
            'id', 'codigo', 'tipo_exame', 'data_coleta', 'hora_coleta'
        )
        read_only = (
            'id'
        )
