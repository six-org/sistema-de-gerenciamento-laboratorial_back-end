from rest_framework import viewsets
from ..models import Etiqueta
from .serializers import EtiquetaSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class EtiquetaModelViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated(), IsAdminUser()]
