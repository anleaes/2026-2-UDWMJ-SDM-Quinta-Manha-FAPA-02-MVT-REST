from django.urls import path
from . import views

app_name = 'divulgacao_evento'

urlpatterns = [
    path('criar/', views.criar_divulgacao_evento, name='criar_divulgacao_evento'),
    path('listar/', views.lista_divulgacao_eventos, name='lista_divulgacao_eventos'),
]