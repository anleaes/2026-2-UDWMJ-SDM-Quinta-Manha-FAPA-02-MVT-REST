from django.urls import path, include
from . import views

app_name = 'funcionario'

urlpatterns = [
    path('criar/', views.criar_funcionario, name='criar_funcionario'),
    path('listar/', views.listar_funcionarios, name='listar_funcionarios'),
    path('editar/', views.editar_funcionario, name='editar_funcionario'),
    
]