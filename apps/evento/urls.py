from django.urls import path
from . import views

app_name = 'evento'

urlpatterns = [
    path('criar/', views.criar_evento, name='criar_evento')
]