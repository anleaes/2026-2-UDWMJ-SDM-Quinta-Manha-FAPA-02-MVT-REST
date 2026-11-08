from django.urls import path
from . import views

app_name = 'espectador'

urlpatterns = [
    path('criar/', views.criar_espectador, name='criar_espectador'),
    
]