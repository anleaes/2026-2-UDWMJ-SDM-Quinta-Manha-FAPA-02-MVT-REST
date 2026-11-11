from django.urls import path
from . import views

app_name= 'cupom'

urlpatterns = [
    path('criar/', views.criar_cupom, name='criar_cupom'),
    path('lista/', views.lista_cupom, name='lista_cupom'),
]