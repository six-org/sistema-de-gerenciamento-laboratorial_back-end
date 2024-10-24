from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from gerenciamento_laboratorial.users.api.views import UserViewSet
from gerenciamento_laboratorial.etiqueta.api.views import EtiquetaModelViewSet
from django.urls import path, include
from gerenciamento_laboratorial.paciente.api.views import PacienteViewSet
from gerenciamento_laboratorial.exame.api.views import ExameViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet, basename="users")
router.register("etiqueta", EtiquetaModelViewSet, basename="etiqueta")
router.register('exame', ExameViewSet, basename='exame')

app_name = "api"
urlpatterns = router.urls

api_router = DefaultRouter()
api_router.register(r'pacientes', PacienteViewSet, basename='pacientes')

urlpatterns = [
    path('api/', include(api_router.urls)),
]
