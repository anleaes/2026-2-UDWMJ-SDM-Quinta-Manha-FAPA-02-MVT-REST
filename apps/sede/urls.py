from django.urls import path, include
from . import views

from rest_framework import routers

app_name = 'sede'

router = routers.SimpleRouter()
router.register('', views.SedeViewSet, basename='sede')

urlpatterns = [
    path('criar/', views.criar_sede, name='criar_sede'),
    path('listar/', views.listar_sedes, name='listar_sedes'),
    path('editar/<int:sede_id>/', views.editar_sede, name='editar_sede'),
    path('deletar/<int:sede_id>/', views.deletar_sede, name='deletar_sede'),

]