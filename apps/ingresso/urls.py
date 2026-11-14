from django.urls import path
from . import views

app_name = 'ingresso'

urlpatterns = [
    path('criar/', views.criar_ingresso, name='criar_ingresso'),
    path('listar/', views.lista_ingresso, name='lista_ingresso'),
    path('editar/<int:id_ingresso>/', views.editar_ingresso, name='editar_ingresso'),
    path('deletar/<int:id_ingresso>/', views.deletar_ingresso, name='deletar_ingresso'),
]