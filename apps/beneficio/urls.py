from django.urls import path, include
from . import views

app_name = 'beneficio'

urlpatterns = [
    path('criar/', views.criar_beneficio, name='criar_beneficio')
]