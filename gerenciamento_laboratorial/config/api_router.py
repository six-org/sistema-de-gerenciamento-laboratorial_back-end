from rest_framework.routers import DefaultRouter
from gerenciamento_laboratorial.users.api.views import UserViewSet
from gerenciamento_laboratorial.etiqueta.api.views import EtiquetaModelViewSet
from gerenciamento_laboratorial.paciente.api.views import PacienteViewSet
from gerenciamento_laboratorial.insumo.api.views import InsumoModelViewSet
from gerenciamento_laboratorial.exame.api.views import ExameViewSet
from gerenciamento_laboratorial.funcionario.api.views import FuncionarioViewSet
from gerenciamento_laboratorial.atendimento.api.views import AtendimentoViewSet

router = DefaultRouter()

# Registro das rotas da API
router.register("users", UserViewSet, basename="users")
router.register("etiqueta", EtiquetaModelViewSet, basename="etiqueta")
router.register("pacientes", PacienteViewSet, basename="pacientes")
router.register("exame", ExameViewSet, basename="exame")
router.register("funcionarios", FuncionarioViewSet, basename="funcionarios")
router.register("insumo", InsumoModelViewSet, basename="insumo")
router.register("atendimento", AtendimentoViewSet, basename="atendimento")

api_router = router
