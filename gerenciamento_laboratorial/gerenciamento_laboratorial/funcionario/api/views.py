from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from gerenciamento_laboratorial.funcionario.models import Funcionario
from gerenciamento_laboratorial.funcionario.api.serializers import FuncionarioSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        """ RF007 - Cadastrar funcionário """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Funcionário cadastrado com sucesso!"}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """ RF008 - Editar funcionário """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Funcionário atualizado com sucesso!"})

    def retrieve(self, request, *args, **kwargs):
        """ RF009 - Visualizar funcionário """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """ RF010 - Buscar e listar funcionários """
        nome_completo = request.query_params.get('nome_completo', None)
        cpf = request.query_params.get('cpf', None)
        cargo = request.query_params.get('cargo', None)

        queryset = self.get_queryset()

        if nome_completo:
            queryset = queryset.filter(nome_completo__icontains=nome_completo)
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)
        if cargo:
            queryset = queryset.filter(nivel_acesso__icontains=cargo)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
