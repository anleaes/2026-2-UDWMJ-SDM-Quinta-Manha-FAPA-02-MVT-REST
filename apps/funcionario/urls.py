from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'funcionario'

router = routers.SimpleRouter()

urlpatterns = [
    path('criar/', views.criar_funcionario, name='criar_funcionario'),
    path('listar/', views.listar_funcionarios, name='listar_funcionarios'),
    path('editar/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
    path('deletar/<int:funcionario_id>/', views.deletar_funcionario, name='deletar_funcionario'),
    
]