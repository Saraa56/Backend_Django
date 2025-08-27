from rest_framework.routers import DefaultRouter

from .views import ModeradorViewSet, UsuarioViewSet, ReporteViewSet, SectorViewSet

router = DefaultRouter()
router.register(r'moderador', ModeradorViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'reporte', ReporteViewSet)
router.register(r'sector', SectorViewSet)

urlpatterns = router.urls