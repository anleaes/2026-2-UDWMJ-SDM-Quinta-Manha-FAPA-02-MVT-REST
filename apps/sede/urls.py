from django.urls import path, include
from . import views

from rest_framework import routers
from .views import SedeViewSet

app_name = 'sede'

urlpatterns = [
    path('criar/', views.criar_sede, name='criar_sede'),
    path('listar/', views.listar_sedes, name='listar_sedes'),
    path('editar/<int:sede_id>/', views.editar_sede, name='editar_sede'),
    path('deletar/<int:sede_id>/', views.deletar_sede, name='deletar_sede'),

]