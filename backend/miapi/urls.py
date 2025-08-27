from rest_framework.routers import DefaultRouter

from .views import ModeradorViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'moderador', ModeradorViewSet)
router.register(r'usuario', UsuarioViewSet)

urlpatterns = router.urls