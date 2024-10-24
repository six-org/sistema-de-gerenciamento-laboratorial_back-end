from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from gerenciamento_laboratorial.paciente.models import Paciente
from .serializers import PacienteSerializer
from rest_framework.permissions import IsAuthenticated

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados

    # Sobrescrevendo o método para criar paciente
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Paciente cadastrado com sucesso!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

    # Listar pacientes
    def list(self, request, *args, **kwargs):
        pacientes = self.get_queryset()
        serializer = self.get_serializer(pacientes, many=True)
        return Response(serializer.data)

    # Buscar Paciente por Nome ou CPF
    @action(detail=False, methods=['get'], url_path='buscar')
    def buscar_paciente(self, request):
        nome = request.query_params.get('nome_completo', None)
        cpf = request.query_params.get('cpf', None)
        queryset = self.get_queryset()

        if nome:
            queryset = queryset.filter(nome_completo__icontains=nome)
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)

        if not queryset:
            return Response({"message": "Nenhum paciente encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Editar paciente
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Dados do paciente atualizados com sucesso!',
            'data': serializer.data
        })
