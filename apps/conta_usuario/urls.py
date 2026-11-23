from django.urls import path, include
from . import views

app_name = 'conta_usuario'

urlpatterns = [
    path('login/', views.login_usuario, name='login_usuario'),
    path('desconectar/', views.desconectar_usuario, name='desconectar_usuario'),
    path('trocar_senha/', views.trocar_senha_usuario, name='trocar_senha_usuario'),
    path('nao_autorizado/', views.tela_erro_autorizacao, name='tela_erro_autorizacao'),

]