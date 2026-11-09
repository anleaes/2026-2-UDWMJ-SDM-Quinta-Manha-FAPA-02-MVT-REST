from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Beneficio
from .forms import BeneficioForm

def criar_beneficio(request: HttpRequest):
    template_name = 'beneficio/criar_beneficio.html'
    context = {}

    if request.method == 'POST':
        form = BeneficioForm(request.POST)
        if form.is_valid():
            obj_beneficio = form.save(commit=False)
            obj_beneficio.save()
            form.save_m2m()
            return HttpResponse('Sucesso')

    form = BeneficioForm()
    context = { 'form': form }

    return render(request, template_name, context)


def editar_beneficio(request: HttpRequest, beneficio_id: int):
    template_name = 'beneficio/criar_beneficio.html'
    obj_beneficio = get_object_or_404(Beneficio, id=beneficio_id)

    if request.method == 'POST':
        form = BeneficioForm(request.POST, instance=obj_beneficio)
        if form.is_valid():
            form.save()
            return HttpResponse('Sucesso')

    form = BeneficioForm(instance=obj_beneficio)
    context = { 'form': form}
    return render(request, template_name, context)


def listar_beneficios(request: HttpRequest):
    template_name = 'beneficio/listar_beneficios.html'
    beneficios = Beneficio.objects.all()
    context = {'beneficios': beneficios}
    return render(request, template_name, context)

