from django.urls import path, include
from . import views

app_name = 'beneficio'

urlpatterns = [
    path('criar/', views.criar_beneficio, name='criar_beneficio'),
    path('listar/', views.listar_beneficios, name='listar_beneficios'),
    path('editar/<int:beneficio_id>', views.editar_beneficio, name='editar_beneficio'),
    path('deletar/<int:beneficio_id>', views.deletar_beneficio, name='deletar_beneficio'),

]