from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.IngressoViewSet, basename='ingresso')

app_name = 'ingresso'

urlpatterns = [
    path('criar/', views.criar_ingresso, name='criar_ingresso'),
    path('lista/', views.lista_ingresso, name='lista_ingresso'),
    path('editar/<int:id_ingresso>/', views.editar_ingresso, name='editar_ingresso'),
    path('deletar/<int:id_ingresso>/', views.deletar_ingresso, name='deletar_ingresso'),
    path('', include(router.urls))
]