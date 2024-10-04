from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Funcionario
from .forms import FuncionarioForm, UserForm
from django.contrib import messages
from django.db.models import Q

# [RF007] - Cadastrar Funcionário
def cadastrar_funcionario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        funcionario_form = FuncionarioForm(request.POST)
        if user_form.is_valid() and funcionario_form.is_valid():
            user = user_form.save()
            funcionario = funcionario_form.save(commit=False)
            funcionario.user = user
            funcionario.save()
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return redirect('listar_funcionarios')  # Redireciona para a lista de funcionários
    else:
        user_form = UserForm()
        funcionario_form = FuncionarioForm()
    
    return render(request, 'funcionarios/cadastrar_funcionario.html', {
        'user_form': user_form,
        'funcionario_form': funcionario_form
    })

# [RF008] - Editar Funcionário
def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    user = funcionario.user

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        funcionario_form = FuncionarioForm(request.POST, instance=funcionario)
        if user_form.is_valid() and funcionario_form.is_valid():
            user_form.save()
            funcionario_form.save()
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return redirect('listar_funcionarios')  # Redireciona para a lista de funcionários
    else:
        user_form = UserForm(instance=user)
        funcionario_form = FuncionarioForm(instance=funcionario)

    return render(request, 'funcionarios/editar_funcionario.html', {
        'user_form': user_form,
        'funcionario_form': funcionario_form
    })

# [RF009] - Visualizar Funcionário
def visualizar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionarios/visualizar_funcionario.html', {
        'funcionario': funcionario
    })

# [RF010] - Buscar Funcionário
def buscar_funcionario(request):
    query = request.GET.get('q')
    resultados = None
    if query:
        resultados = Funcionario.objects.filter(
            Q(user_first_name_icontains=query) | 
            Q(user_last_name_icontains=query) | 
            Q(user_username_icontains=query) | 
            Q(cargo__icontains=query)
        )
    return render(request, 'funcionarios/buscar_funcionario.html', {
        'resultados': resultados
    })

# Listar Funcionários (para facilitar navegação)
def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/listar_funcionarios.html', {'funcionarios': funcionarios})
