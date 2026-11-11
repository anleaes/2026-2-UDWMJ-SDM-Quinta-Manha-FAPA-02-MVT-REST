from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AssinaturaForm
from .models import Assinatura

from rest_framework import viewsets
from .serializer import AssinaturaSerializer

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

    form = AssinaturaForm()
    context = {'form': form}
    return render(request, template_name, context)

def editar_assinatura(request: HttpRequest, assinatura_id: int):
    template_name = 'assinatura/criar_assinatura.html'
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)

    if request.method == 'POST':
        form = AssinaturaForm(request.POST, request.FILES, instance=assinatura)
        if form.is_valid():
            form.save()
            return redirect('assinatura:listar_assinaturas')

    form = AssinaturaForm(instance=assinatura)
    context = {'form': form}
    return render(request, template_name, context) 


def listar_assinaturas(request: HttpRequest):
    template_name = 'assinatura/listar_assinaturas.html'
    assinaturas = Assinatura.objects.all()
    context = { 'assinaturas': assinaturas}
    return render(request, template_name, context)


def deletar_assinatura(request: HttpRequest, assinatura_id: int):
    obj_assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    obj_assinatura.delete()
    return redirect('assinatura:listar_assinaturas')