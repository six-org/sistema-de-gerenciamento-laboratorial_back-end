from rest_framework import viewsets
from rest_framework import filters
from gerenciamento_laboratorial.insumo.models import Insumo
from .serializer import InsumoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class InsumoModelViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome','quantidade']
    
