from django.urls import path, include
from . import views

app_name = 'conta_usuario'

urlpatterns = [
        path('login/', views.login_usuario, name='login_usuario'),
        
]