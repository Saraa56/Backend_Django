from rest_framework.routers import DefaultRouter

from .views import ModeradorViewSet, UsuarioViewSet, ReporteViewSer

router = DefaultRouter()
router.register(r'moderador', ModeradorViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'reporte', ReporteViewSer)
router.register(r'sector', ReporteViewSer)

urlpatterns = router.urls