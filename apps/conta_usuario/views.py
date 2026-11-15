from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

def login_usuario(request):
    template_name = 'accounts/tela_login.html'
    if request.method =='POST':
        nome_usuario = request.POST.get('usuario')
        senha_digitada = request.POST.get('senha')
        print(nome_usuario)
        print(senha_digitada)
        return HttpResponse('Teste')