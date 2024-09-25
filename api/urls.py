# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet, CategoriasViewSet, ProductoViewSet,
    PedidoViewSet, PedidoProductoViewSet, TallaViewSet, AbonoViewSet
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'categorias', CategoriasViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedido-productos', PedidoProductoViewSet)
router.register(r'tallas', TallaViewSet)
router.register(r'abonos', AbonoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
