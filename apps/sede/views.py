from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Sede
from .forms import SedeForm

def criar_sede(request: HttpRequest):
    template_name = 'sede/criar_sede.html'
    context = {}

    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            obj_sede = form.save(commit=False)
            obj_sede.save()
            form.save_m2m()
            # redirecionar para listar Sedes
            return redirect('index:inicial')

    form = SedeForm()
    context['form'] = form
    return render(request, template_name, context)


def listar_sedes(request: HttpRequest):
    template_name = 'sede/listar_sedes.html'

    sedes = Sede.objects.all()
    context = {
        'sedes': sedes
    }

    return render(request, template_name, context)

def editar_sede(request: HttpRequest, sede_id : int):
    template_name = 'sede/criar_sede.html'
    context = {}
    sede = get_object_or_404(Sede, id=sede_id)

    #O Django diferencia o POST do criar e editar a partir do URL atual que o usuário se encontra!
    if request.method == 'POST':
        form = SedeForm(request.POST, instance=sede)
        if form.is_valid():
            form.save()
            return redirect('sede:listar_sedes')
        
    form = SedeForm(instance=sede)
    context['form'] = form
    return render(request, template_name, context)


