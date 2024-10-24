from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('editar/<uuid:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
    path('visualizar/<uuid:funcionario_id>/', views.visualizar_funcionario, name='visualizar_funcionario'),
    path('buscar/', views.buscar_funcionario, name='buscar_funcionario'),
    path('', views.listar_funcionarios, name='listar_funcionarios'),
]