from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Funcionario
from .forms import FuncionarioForm

from rest_framework import viewsets
from .serializer import FuncionarioSerializer

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def criar_funcionario(request: HttpRequest):
    template_name = 'funcionario/criar_funcionario.html'
    context = {}

    if(request.method == 'POST'):
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            obj_funcionario = form.save(commit=False)
            obj_funcionario.save()
            form.save_m2m()

            #  criacao automatica de conta
            conta_usuario = User(username=obj_funcionario.nome, password='senhapadrao1234')
            conta_usuario.set_password(conta_usuario.password)
            conta_usuario.save()

            # usuario precisa existir no banco de dados (ter um ID) para poder recebem cargos
            grupo_acesso = Group.objects.get(name=f'acesso_{str.lower(obj_funcionario.cargo)}')
            conta_usuario.groups.add(grupo_acesso)
            

            return redirect('funcionario:listar_funcionarios')

    form = FuncionarioForm()
    context['form'] = form
    return render(request, template_name, context)

def listar_funcionarios(request: HttpRequest):
    template_name = 'funcionario/listar_funcionarios.html'
    funcionarios = Funcionario.objects.all()
    context = {
        'funcionarios': funcionarios
    }

    return render(request, template_name, context)

def editar_funcionario(request: HttpRequest, funcionario_id: int):
    template_name = 'funcionario/criar_funcionario.html'
    context = {}
    obj_funcionario = get_object_or_404(Funcionario, id=funcionario_id)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=obj_funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario:listar_funcionarios')

    form = FuncionarioForm(instance=obj_funcionario)
    context = { 
        'form': form
    }
    return render(request, template_name, context)

def deletar_funcionario(request: HttpRequest, funcionario_id: int):
    obj_funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    obj_funcionario.delete()
    return redirect('funcionario:listar_funcionarios')


# ---------------------------- REST -------------------------------------

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer 

     
