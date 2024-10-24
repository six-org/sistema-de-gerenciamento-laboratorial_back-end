from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from gerenciamento_laboratorial.exame.models import Exame
from .serializers import ExameSerializer
from .permissions import IsOwnerExameOrIsStaff
from rest_framework.decorators import action

AGENDAMENTO_STATUS = Exame.AGENDAMENTO_CHOICES[0][0]
AGENDADO_STATUS = Exame.AGENDAMENTO_CHOICES[1][0]
CANCELAMENTO_STATUS = Exame.AGENDAMENTO_CHOICES[2][0]


class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer
    filter_backends = [SearchFilter]
    search_fields = ['paciente__user__name', 'tipo', 'data_hora']

    def get_permissions(self):
        permissions = [IsAuthenticated, IsOwnerExameOrIsStaff]
        if self.action in ['update', 'partial_update', 'create', 'destroy']:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def list(self, request):
        if not request.user.is_staff:
            queryset = self.queryset.filter(paciente=request.user.paciente)
        else:
            queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        exame = Exame.objects.create(**data)
        return Response(self.get_serializer(exame).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        if not request.user.is_staff:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        exame = self.get_object()
        exame.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def list_agendamentos(self, request):
        agendamentos = self.queryset.filter(status=AGENDAMENTO_STATUS)
        serializer = self.get_serializer(agendamentos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def list_cancelamentos(self, request):
        cancelamentos = self.queryset.filter(status=CANCELAMENTO_STATUS)
        serializer = self.get_serializer(cancelamentos, many=True)
        return Response(serializer.data)
