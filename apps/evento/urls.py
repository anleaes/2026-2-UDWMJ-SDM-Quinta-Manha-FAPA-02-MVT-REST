from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.EventoViewSet, basename='evento')

app_name = 'evento'

urlpatterns = [
    path('criar/', views.criar_evento, name='criar_evento'),
    path('listar/', views.lista_eventos, name='listar_eventos'),
    path('editar/<int:id_evento>/', views.editar_evento, name='editar_evento'),
    path('deletar/<int:id_evento>/', views.deletar_evento, name='deletar_evento'),
    path('', include(router.urls))
]