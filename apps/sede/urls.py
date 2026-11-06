from django.urls import path, include
from . import views

app_name = 'sede'

urlpatterns = [
    path('criar/', views.criar_sede, name='criar_sede'),
]