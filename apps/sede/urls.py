from django.urls import path, include
from . import views

app_name = 'sede'

urlpatterns = [
    path('criar/', views.criar_sede, name='criar_sede'),
    path('listar/', views.listar_sedes, name='listar_sedes'),
]