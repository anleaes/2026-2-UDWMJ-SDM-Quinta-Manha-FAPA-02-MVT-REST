from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.VendaViewSet, basename='venda')

app_name = 'venda'

urlpatterns = [
    path('criar/', views.criar_venda, name='criar_venda'),
    path('listar/', views.lista_venda, name='lista_venda'),
    path('editar/<int:id_venda>/', views.editar_venda, name='editar_venda'),
    path('deletar/<int:id_venda>/', views.deletar_venda, name='deletar_venda'),
    path('', include(router.urls))
]