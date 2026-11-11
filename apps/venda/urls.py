from django.urls import path
from . import views

app_name = 'divulgacao_evento'

urlpatterns = [
    path('criar/', views.criar_venda, name='criar_venda'),
]