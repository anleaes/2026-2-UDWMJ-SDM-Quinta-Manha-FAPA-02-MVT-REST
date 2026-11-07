from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Funcionario
from .forms import FuncionarioForm


def criar_funcionario(request: HttpRequest):
    template_name = 'funcionario/criar_funcionario.html'
    context = {}

    if(request.method == 'POST'):
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            obj_funcionario = form.save(commit=False)
            obj_funcionario.save()
            form.save_m2m()
            return HttpResponse('Sucesso')

    form = FuncionarioForm()
    context['form'] = form
    return render(request, template_name, context)
