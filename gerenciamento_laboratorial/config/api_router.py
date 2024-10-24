from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from gerenciamento_laboratorial.users.api.views import UserViewSet
from gerenciamento_laboratorial.etiqueta.api.views import EtiquetaModelViewSet
router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet, basename="users")
router.register("etiqueta", EtiquetaModelViewSet, basename="etiqueta")

app_name = "api"
urlpatterns = router.urls
