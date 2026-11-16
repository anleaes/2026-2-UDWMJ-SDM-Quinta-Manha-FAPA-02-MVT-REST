from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/conta/login/')
@permission_required('pessoa.acesso_atendente')
def inicial(request):
    template_name ='index/inicial.html'
    context = {}

    return render(request, template_name, context)
