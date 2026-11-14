from django.urls import path
from . import views

app_name= 'cupom'

urlpatterns = [
    path('criar/', views.criar_cupom, name='criar_cupom'),
    path('listar/', views.lista_cupom, name='lista_cupom'),
    path('editar/<int:id_cupom>/', views.editar_cupom, name='editar_cupom'),
    path('deletar/<int:id_cupom>/', views.deletar_cupom, name='deletar_cupom'),
]