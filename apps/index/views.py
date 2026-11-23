from django.http import HttpResponse
from django.shortcuts import render

def inicial(request):
    template_name ='index/inicial.html'
    context = {}

    #  exemplo de controle de acesso
    # accesso_permitido = len(request.user.groups.filter(name='acesso_gerente')) > 0
    # if not accesso_permitido:
    #     return HttpResponse('Acesso Negado', status=403)
    
    return render(request, template_name, context)
