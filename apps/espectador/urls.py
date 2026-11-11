from django.urls import path
from . import views
from rest_framework import routers

app_name = 'espectador'




urlpatterns = [
    path('criar/', views.criar_espectador, name='criar_espectador'),
    path('listar/', views.listar_espectadores, name='listar_espectadores'),
    path('editar/<int:espectador_id>', views.editar_espectador, name='editar_espectador'),
    path('deletar/<int:espectador_id>', views.deletar_espectador, name='deletar_espectador'),
]