from django.urls import path
from . import views

app_name = 'divulgacao_evento'

urlpatterns = [
    path('criar/', views.criar_venda, name='criar_venda'),
    path('listar/', views.lista_venda, name='lista_venda'),
    path('editar/<int:id_venda>/', views.editar_venda, name='editar_venda'),
    path('deletar/<int:id_venda>/', views.deletar_venda, name='deletar_venda'),
]