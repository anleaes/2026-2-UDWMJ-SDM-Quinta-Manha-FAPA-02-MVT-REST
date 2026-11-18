from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AssinaturaForm
from .models import Assinatura

from rest_framework import viewsets
from .serializer import AssinaturaSerializer
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/conta/nao_autorizado')
@permission_required('pessoa.acesso_atendente', login_url='/conta/nao_autorizado')
def criar_assinatura(request: HttpRequest):
    template_name = 'assinatura/criar_assinatura.html'
    context = {}

    if request.method == 'POST':
        form = AssinaturaForm(request.POST, request.FILES)
        if form.is_valid():
            obj_assinatura = form.save(commit=False)
            obj_assinatura.save()
            form.save_m2m()
            return redirect('assinatura:listar_assinaturas')
        else:
            context['erros_validacao'] = list(form.errors.items())
            context['form'] = AssinaturaForm(request.POST)
            return render(request, template_name, context)

    form = AssinaturaForm()
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='/conta/nao_autorizado')
@permission_required('pessoa.acesso_gerente', login_url='/conta/nao_autorizado')
def editar_assinatura(request: HttpRequest, assinatura_id: int):
    template_name = 'assinatura/criar_assinatura.html'
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    context = {}

    if request.method == 'POST':
        form = AssinaturaForm(request.POST, request.FILES, instance=assinatura)
        if form.is_valid():
            form.save()
            return redirect('assinatura:listar_assinaturas')
        else:
            context['erros_validacao'] = list(form.errors.items())
            context['form'] = AssinaturaForm(request.POST)
            return render(request, template_name, context)

    form = AssinaturaForm(instance=assinatura)
    context = {'form': form}
    return render(request, template_name, context) 

@login_required(login_url='/conta/nao_autorizado')
@permission_required('pessoa.acesso_atendente', login_url='/conta/nao_autorizado')
def listar_assinaturas(request: HttpRequest):
    template_name = 'assinatura/listar_assinaturas.html'
    assinaturas = Assinatura.objects.all()
    context = { 'assinaturas': assinaturas}
    return render(request, template_name, context)

@login_required(login_url='/conta/nao_autorizado')
@permission_required('pessoa.acesso_gerente', login_url='/conta/nao_autorizado')
def deletar_assinatura(request: HttpRequest, assinatura_id: int):
    obj_assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    obj_assinatura.delete()
    return redirect('assinatura:listar_assinaturas')


# ------------------ REST -------------------------------------
class AssinaturaViewSet(viewsets.ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer