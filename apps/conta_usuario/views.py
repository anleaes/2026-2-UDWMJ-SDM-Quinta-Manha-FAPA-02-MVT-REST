from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


def login_usuario(request):
    template_name = 'conta_usuario/tela_login.html'

    if request.method =='POST':
        nome_usuario = request.POST.get('usuario')
        senha_digitada = request.POST.get('senha')
        usuario = authenticate(username=nome_usuario, password=senha_digitada)

        if usuario is not None:
            login(request, usuario)
            return redirect(request.GET.get('next', '/'))
        else:
            return redirect('conta_usuario:login_usuario')

    context = {}
    return render(request, template_name, context)

def desconectar_usuario(request):
    logout(request)
    return redirect('conta_usuario:login_usuario')

def tela_erro_autorizacao(request):
    template_name = 'conta_usuario/tela_erro_autorizacao.html'
    context = {}
    return render(request, template_name, context)


@login_required(login_url='/conta/login/')
def trocar_senha_usuario(request):
    template_name = 'conta_usuario/trocar_senha.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            return redirect('conta:login_usuario')
    form = PasswordChangeForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, template_name, context)