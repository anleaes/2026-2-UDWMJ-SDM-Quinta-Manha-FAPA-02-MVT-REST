from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.Cartao_VipSerializer, basename='cartao_vip')

app_name = 'cartao_vip'

urlpatterns = [
    path('criar/', views.criar_cartao_vip, name='criar_cartao_vip'),
    path('listar/', views.lista_cartao_vip, name='lista_cartao_vip'),
    path('editar/<int:id_cartao_vip>/', views.editar_cartao_vip, name='editar_cartao_vip'),
    path('deletar/<int:id_cartao_vip>/', views.deletar_cartao_vip, name='deletar_cartao_vip'),
    path('', include(router.urls))
]