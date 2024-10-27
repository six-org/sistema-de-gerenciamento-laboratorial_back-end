from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


from ..models import Atendimento
from .serializers import AtendimentoSerializer


class AtendimentoViewSet(viewsets.ModelViewSet):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer
    permission_classes = [IsAdminUser]
