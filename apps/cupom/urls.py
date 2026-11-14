from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.CupomViewSet, basename='cupom')

app_name= 'cupom'

urlpatterns = [
    path('criar/', views.criar_cupom, name='criar_cupom'),
    path('lista/', views.lista_cupom, name='lista_cupom'),
    path('editar/<int:id_cupom>/', views.editar_cupom, name='editar_cupom'),
    path('deletar/<int:id_cupom>/', views.deletar_cupom, name='deletar_cupom'),
    path('', include(router.urls))
]