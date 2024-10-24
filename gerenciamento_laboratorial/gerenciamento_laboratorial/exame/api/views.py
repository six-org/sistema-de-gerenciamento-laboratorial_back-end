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
        if self.action in ['update', 'partial_update']:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    def list(self, request):
        if not request.user.is_staff:
            return self.queryset.filter(paciente=request.user.paciente,
                                        status=AGENDADO_STATUS)
        return super().list(request)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if request.user.is_staff:
            data['status'] = AGENDADO_STATUS
        exame = Exame.objects.create(**data)
        return Response(self.get_serializer(exame).data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        if not request.user.is_staff:
            exame = self.get_object()
            exame.status = CANCELAMENTO_STATUS
            exame.save()
            return Response(
                data={'detail': 'Solicitação de cancelamento realizada'},
                status=status.HTTP_200_OK)
        return super().destroy(request, pk)

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def list_agendamentos(self, request):
        return self.queryset.filter(status=AGENDAMENTO_STATUS)

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def list_cancelamentos(self, request):
        return self.queryset.filter(status=CANCELAMENTO_STATUS)
