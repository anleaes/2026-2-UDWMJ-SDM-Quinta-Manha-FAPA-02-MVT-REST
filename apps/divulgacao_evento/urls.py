from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.Divulgacao_EventoViewSet, basename='divulgacao_evento')



app_name = 'divulgacao_evento'

urlpatterns = [
    path('criar/', views.criar_divulgacao_evento, name='criar_divulgacao_evento'),
    path('listar/', views.lista_divulgacao_eventos, name='lista_divulgacao_evento'),
    path('editar/<int:id_divulgacao_evento>/', views.editar_divulgacao_evento, name='editar_divulgacao_evento'),
    path('deletar/<int:id_divulgacao_evento>/', views.deletar_divulgacao_evento, name='deletar_divulgacao_evento'),
    path('', include(router.urls))
]