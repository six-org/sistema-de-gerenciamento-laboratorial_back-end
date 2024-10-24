from rest_framework import serializers
from django.contrib.auth.models import User
from gerenciamento_laboratorial.funcionario.models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome_completo', 'cpf', 'data_nascimento', 'nivel_acesso', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extrai os dados do usuário
        # Verifica se o nome de usuário já existe
        if User.objects.filter(username=user_data['username']).exists():
            raise serializers.ValidationError("Este nome de usuário já está em uso.")
        
        # Cria o usuário associado ao funcionário
        user = User.objects.create_user(**user_data)  # Use create_user para garantir criação correta
        funcionario = Funcionario.objects.create(user=user, **validated_data)
        return funcionario

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        user = instance.user

        # Atualiza os dados do Funcionario
        instance.nome_completo = validated_data.get('nome_completo', instance.nome_completo)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.nivel_acesso = validated_data.get('nivel_acesso', instance.nivel_acesso)
        instance.save()

        # Atualiza os dados do User se fornecidos
        if user_data:
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.save()

        return instance

    def validate_cpf(self, value):
        """ Valida o CPF para garantir que é único e tem o formato correto. """
        if self.instance:  # Se estiver atualizando, evita erro ao comparar com o próprio CPF
            if Funcionario.objects.filter(cpf=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Este CPF já está em uso.")
        else:
            if Funcionario.objects.filter(cpf=value).exists():
                raise serializers.ValidationError("Este CPF já está em uso.")
        return value
