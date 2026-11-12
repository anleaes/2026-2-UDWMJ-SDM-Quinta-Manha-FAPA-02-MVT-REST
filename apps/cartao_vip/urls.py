from django.urls import path
from . import views

app_name = 'cartao_vip'

urlpatterns = [
    path('criar/', views.criar_cartao_vip, name='criar_cartao_vip'),
    path('listar/', views.lista_cartao_vip, name='lista_cartao_vip'),
    path('editar/<int:id_cartao_vip>/', views.editar_cartao_vip, name='editar_cartao_vip'),
]