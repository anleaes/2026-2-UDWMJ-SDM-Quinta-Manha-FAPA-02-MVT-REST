from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Evento

def criar_evento(request):
    template_name='evento/criar_evento.html'
    context= {}

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            #TODO: retornar para o core
        form = EventoForm()
        context['form'] = form
        return render(request, template_name, context)