from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EspectadorForm

def criar_espectador(request: HttpRequest):
    template_name = 'espectador/criar_espectador.html'
    context = {}

    if request.method == 'POST':
        form = EspectadorForm(request.POST)

        if form.is_valid():
            obj_espectador = form.save(commit=False)
            obj_espectador.save()
            form.save_m2m()
            return HttpResponse('Sucesso')

    form = EspectadorForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
