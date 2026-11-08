from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EspectadorForm
from .models import Espectador

def criar_espectador(request: HttpRequest):
    template_name = 'espectador/criar_espectador.html'
    context = {}

    if request.method == 'POST':
        form = EspectadorForm(request.POST)

        if form.is_valid():
            obj_espectador = form.save(commit=False)
            obj_espectador.save()
            form.save_m2m()
            return redirect('espectador:listar_espectadores')

    form = EspectadorForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def listar_espectadores(request: HttpRequest):
    template_name = 'espectador/listar_espectadores.html'
    espectadores = Espectador.objects.all()
    context = {'espectadores': espectadores}
    return render(request, template_name, context)


def editar_espectador(request: HttpRequest, espectador_id: int):
    template_name = 'espectador/criar_espectador.html'
    obj_espectador = get_object_or_404(Espectador, id=espectador_id)

    if request.method == 'POST':
        form = EspectadorForm(request.POST, instance=obj_espectador)
        if form.is_valid():
            form.save()
            return redirect('espectador:listar_espectadores')

    form = EspectadorForm(instance=obj_espectador)
    context = { 'form': form}
    return render(request, template_name, context)
