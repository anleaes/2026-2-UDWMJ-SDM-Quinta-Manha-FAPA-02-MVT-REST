from django.urls import path
from . import views

app_name = 'ingresso'

urlpatterns = [
    path('criar/', views.criar_ingresso, name='criar_ingresso'),
    path('lista/', views.lista_ingresso, name='lista_ingresso'),
]