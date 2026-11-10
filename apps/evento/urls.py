from django.urls import path
from . import views

app_name = 'evento'

urlpatterns = [
    path('criar/', views.criar_evento, name='criar_evento'),
    path('listar/', views.lista_eventos, name='listar_eventos'),
    path('editar/<int:id_evento>/', views.editar_evento, name='editar_evento'),
    path('deletar/<int:id_evento>/', views.deletar_evento, name='deletar_evento'),
]