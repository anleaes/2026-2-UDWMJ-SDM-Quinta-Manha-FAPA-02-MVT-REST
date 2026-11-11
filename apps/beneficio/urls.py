from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'beneficio'

router = routers.SimpleRouter()

urlpatterns = [
    path('criar/', views.criar_beneficio, name='criar_beneficio'),
    path('listar/', views.listar_beneficios, name='listar_beneficios'),
    path('editar/<int:beneficio_id>', views.editar_beneficio, name='editar_beneficio'),
    path('deletar/<int:beneficio_id>', views.deletar_beneficio, name='deletar_beneficio'),

]