from django.urls import path
from . import views
from rest_framework import routers

app_name = 'assinatura'

router = routers.SimpleRouter()



urlpatterns = [
    path('criar/', views.criar_assinatura, name='criar_assinatura'),
    path('listar/', views.listar_assinaturas, name='listar_assinaturas'),
    path('editar/<int:assinatura_id>', views.editar_assinatura, name='editar_assinatura'),
    path('deletar/<int:assinatura_id>', views.deletar_assinatura, name='deletar_assinatura'),
    
]