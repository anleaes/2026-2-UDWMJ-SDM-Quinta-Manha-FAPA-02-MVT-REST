from django.urls import path
from . import views

app_name = 'assinatura'

urlpatterns = [
    path('criar/', views.criar_assinatura, name='criar_assinatura'),
    path('editar/<int:assinatura_id>', views.editar_assinatura, name='editar_assinatura'),
    
]